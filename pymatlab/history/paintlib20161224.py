# -*- coding: utf-8 -*-
#
import pya
from math import *
import time

class BasicPainter:#用于画基础图形的静态类
    @staticmethod
    def rectangle(pointr,pointl,length):
        #给定矩形的右下pointr左下pointl画出指定长度矩形
        #pointr,pointl,pointl2,pointr2        
        #x1,y1,x2,y2,length,path
        delta=pointr.distance(pointl)
        xx=length/delta*(pointl.y-pointr.y)
        yy=length/delta*(pointr.x-pointl.x)
        pointl2=pya.DPoint(pointl.x+xx,pointl.y+yy)
        pointr2=pya.DPoint(pointr.x+xx,pointr.y+yy)
        rectangle1=pya.DPolygon([pointr,pointl,pointl2,pointr2])
        return rectangle1,pointr2,pointl2
    @staticmethod
    def arc(point0,r,n,angle0,angle1):
        arcpointlist=[]
        angles=[angle0+1.0*x/(n-1)*(angle1-angle0) for x in range(n)]
        for angle in angles:
            arcpointlist.append(pya.DPoint(point0.x+r*cos(angle*pi/180),point0.y+r*sin(angle*pi/180)))            
        return arcpointlist        
    @staticmethod
    def thickarc(point0,rr,rl,n,angle0,angle1):
        thickarcpointlist=[]
        thickarcpointlist.extend(BasicPainter.arc(point0,rr,n,angle0,angle1))
        thickarcpointlist.extend(BasicPainter.arc(point0,rl,n,angle1,angle0))
        thickarc1=pya.DPolygon(thickarcpointlist)
        return thickarc1,thickarcpointlist[n-1],thickarcpointlist[n]
    @staticmethod
    def NewtonInterpolation(X,Y,high):
        n=len(X)
        a=[Y[0]]
        d=[]
        for j in range(n-1):
            d2=d
            if j==0:
                d2=Y
            d=[]
            for k in range(n-1-j):
                if X[k+j+1]==X[k]:
                    d.append(high.pop(0))
                else:
                    d.append((d2[k+1]-d2[k])/(X[k+j+1]-X[k]))
            a.append(d[0])
        def f(x):
            y=a[0]
            Df=1.0
            for j in range(1,n):
                Df*=(x-X[j-1])
                y+=a[j]*Df
            return y
        return f    
    @staticmethod
    def arc_NewtonInterpolation(n,r1,r2):
        thetax=0.53977;
        thetay=-thetax*tan(pi/180*67.5)
        X=[-1,-1,-1,-thetax,0,thetax,1,1,1]
        Y=[-1,-1,-1,thetay,-sqrt(2),thetay,-1,-1,-1]
        high=[-1,-1,1,1,   0,0]
        f=BasicPainter.NewtonInterpolation(X,Y,high)
        pts1=[]
        pts2=[]        
        for i in range(n):
            x=-1.0+2.0/(n-1)*i
            pts1.append(pya.DPoint(x/sqrt(2)*r1,f(x)/sqrt(2)*r1))
            pts2.append(pya.DPoint(x/sqrt(2)*r2,f(x)/sqrt(2)*r2))
        pts1.extend(reversed(pts2))
        return pya.DPolygon(pts1)
        
class Painter(object):
    pass
#cell.shapes(layer1).insert(pya.Polygon.from_dpoly(pya.DPolygon(pts)))

class CavityPainter(Painter):
    def __init__(self,pointr=pya.DPoint(0,1000),pointl=pya.DPoint(0,0)):
        self.outputlist=[];        
        self.pointr=pointr
        self.pointl=pointl
        self.Turning=self.TurningArc
        self.pointdistance=500
        #沿着前进方向，右边pointr，左边pointl
    def Setpoint(self,pointr=pya.DPoint(0,1000),pointl=pya.DPoint(0,0)):       
        self.pointr=pointr
        self.pointl=pointl
    def Straight(self,length):
        rectangle1,self.pointr,self.pointl=BasicPainter.rectangle(self.pointr,self.pointl,length)
        self.outputlist.append(rectangle1)
    def TurningArc(self,radius,angle=90):
        #radius非负向右，负是向左
        delta=self.pointr.distance(self.pointl)
        dx=(self.pointr.x-self.pointl.x)/delta
        dy=(self.pointr.y-self.pointl.y)/delta
        dtheta=atan2(dy,dx)*180/pi
        centerx=self.pointr.x+(radius-delta/2)*dx
        centery=self.pointr.y+(radius-delta/2)*dy
        center=pya.DPoint(centerx,centery)
        n=ceil((abs(radius)+delta/2)*angle*pi/180/self.pointdistance)+2        
        if radius>=0:
            thickarc1,pointr2,pointl2=BasicPainter.thickarc(center,radius-delta/2,radius+delta/2,n,dtheta+180,dtheta+180-angle)
        else:
            thickarc1,pointr2,pointl2=BasicPainter.thickarc(center,-radius+delta/2,-radius-delta/2,n,dtheta,dtheta+angle)
        self.outputlist.append(thickarc1)
        self.pointr=pointr2
        self.pointl=pointl2
    def TurningInterpolation(self,radius):
        #radius非负向右，负是向左
        angle=90
        delta=self.pointr.distance(self.pointl)
        dx=(self.pointr.x-self.pointl.x)/delta
        dy=(self.pointr.y-self.pointl.y)/delta
        dtheta=atan2(dy,dx)*180/pi
        centerx=self.pointr.x+(radius-delta/2)*dx
        centery=self.pointr.y+(radius-delta/2)*dy        
        n=ceil(1.3*(abs(radius)+delta/2)*angle*pi/180/self.pointdistance)+2
        if True:
            rsgn=(radius>0)-(radius<0)
            pointr2=pya.DPoint(centerx-rsgn*(radius-delta/2)*dy,centery+rsgn*(radius-delta/2)*dx)
            pointl2=pya.DPoint(centerx-rsgn*(radius+delta/2)*dy,centery+rsgn*(radius+delta/2)*dx)
            arc1=BasicPainter.arc_NewtonInterpolation(n,abs(radius)+delta/2,abs(radius)-delta/2)
            trans=pya.DCplxTrans(1,180+dtheta+45*rsgn,False,centerx,centery)
            arc1.transform(trans)
            self.outputlist.append(arc1)
            self.pointr=pointr2
            self.pointl=pointl2
    def Output(self,cell,layer):
        for x in self.outputlist:
            if isinstance(x,pya.DPolygon):
                cell.shapes(layer).insert(pya.Polygon.from_dpoly(x))
            else:
                cell.shapes(layer).insert(x)
        self.outputlist=[]
    def Output_Region(self):
        polygons=[]
        for x in self.outputlist:
            if isinstance(x,pya.DPolygon):
                polygons.append(pya.Polygon.from_dpoly(x))
        self.outputlist=[]
        return pya.Region(polygons)

class ObjectPainter(Painter):
    def __init__(self):
        self.outputlist=[];
        self.Basic = pya.Library.library_by_name("Basic")
        self.TEXT_decl = self.Basic.layout().pcell_declaration("TEXT");
    def Output(self,cell,layer):
        for x in self.outputlist:
            cell.shapes(layer).insert(pya.Polygon.from_dpoly(x))
        self.outputlist=[]
    def DrawBorder(self,wed=50000,leng=3050000,siz=3050000):
        pts=[pya.DPoint(-siz,-siz),pya.DPoint(-siz+leng,-siz),pya.DPoint(-siz+leng,-siz+wed)]
        pts.extend([pya.DPoint(-siz+wed,-siz+wed),pya.DPoint(-siz+wed,-siz+leng),pya.DPoint(-siz,-siz+leng)])
        self.outputlist.append(pya.DPolygon(pts))
        for i in pts:
            i.x=-i.x
        self.outputlist.append(pya.DPolygon(pts))
        for i in pts:
            i.y=-i.y
        self.outputlist.append(pya.DPolygon(pts))
        for i in pts:
            i.x=-i.x
        self.outputlist.append(pya.DPolygon(pts))
    def DrawText(self,textstr,DCplxTrans1,cell,layer1,layout):
        #左下角坐标,每个字宽0.6*倍数高0.7*倍数  
        #tr=pya.DCplxTrans(1,0,False,0,0)
        #倍数,逆时针度数,是否绕x翻转,平移x,平移y
        tr=pya.CplxTrans.from_dtrans(DCplxTrans1)       
        param = { 
            "text": textstr, 
            "layer": layer1, 
            "mag": 1 
        }
        pv = []
        for p in self.TEXT_decl.get_parameters():
            if p.name in param:
                pv.append(param[p.name])
            else:
                pv.append(p.default)
        text_cell = layout.create_cell(textstr)
        self.TEXT_decl.produce(layout, [ layer1 ], pv, text_cell)        
        cell.insert(pya.CellInstArray(text_cell.cell_index(), tr))
        return list(pya.DPolygon([pya.DPoint(0,0),pya.DPoint(0,0.7),pya.DPoint(len(textstr)*0.6,0.7)
        ,pya.DPoint(len(textstr)*0.6,0)]).transformed(DCplxTrans1).each_point_hull())
    def Drawxxx(self):
        pts=[]
        pts.append(pya.DPoint(-501000,-225000))
        pts.append(pya.DPoint(-621000,-8000))
        pts.append(pya.DPoint(-625000,-8000))
        pts.append(pya.DPoint(-625000,-4000))
        pts.append(pya.DPoint(-621000,-4000))
        pts.append(pya.DPoint(-501000,-125000))
        pts.append(pya.DPoint(-251000,-125000))
        pts.append(pya.DPoint(-251000,125000))
        pts.append(pya.DPoint(-501000,125000))
        pts.append(pya.DPoint(-621000,4000))
        pts.append(pya.DPoint(-625000,4000))
        pts.append(pya.DPoint(-625000,8000))
        pts.append(pya.DPoint(-621000,8000))
        pts.append(pya.DPoint(-501000,225000))
        pts.append(pya.DPoint(-186000,225000))
        pts.append(pya.DPoint(-186000,5000))
        pts.append(pya.DPoint(0,5000))
        pts.append(pya.DPoint(0,-5000))
        pts.append(pya.DPoint(-186000,-5000))
        pts.append(pya.DPoint(-186000,-225000))
        self.outputlist.append(pya.DPolygon(pts))
        return [pya.DPoint(-625000,8000),pya.DPoint(-625000,4000),pya.DPoint(-625000,-4000),pya.DPoint(-625000,-8000)]

class TransfilePainter(Painter):
    #此对象尚未测试
    def __init__(self,layout):
        self.layout=layout
        self.filename="[insert].gds"
        self.insertcellname="insert"
    def DrawAirbridge(self,cell,Centerlinelist):
        pass
    def DrawMark(self,cell,pts):
        self.layout.read(self.filename)
        for i in self.layout.top_cells():
            if (i.name == self.insertcellname):
              i.name="Mark"
              for pt in pts:
                  tr=pya.Trans(pt.x,pt.y)
                  new_instance=pya.CellInstArray(i.cell_index(),tr)
                  cell.insert(new_instance)
    def DrawGds(self,cell,DCplxTrans1,newcellname):
        #tr=pya.DCplxTrans(1,0,False,0,0)
        #倍数,逆时针度数,是否绕x翻转,平移x,平移y
        tr=pya.CplxTrans.from_dtrans(DCplxTrans1)
        self.layout.read(self.filename)
        for i in self.layout.top_cells():
            if (i.name == self.insertcellname):
              i.name=newcellname
              new_instance=pya.CellInstArray(i.cell_index(),tr)
              cell.insert(new_instance)

class IOsettings:
    @staticmethod
    def Getfilename():
        strtime=time.strftime("%Y%m%d_%H%M%S")
        print(strtime)
        return "[pythonout%s].gds"%strtime



'''
# -*- coding: utf-8 -*-
#
import paintlib
layout = pya.Layout()
layout.dbu = 0.001
cell = layout.create_cell("Cell")
cell2 = layout.create_cell("Child_Cell")
cell.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))

layer1 = layout.layer(10, 10)
painter3=paintlib.CavityPainter(pya.DPoint(0,0),pya.DPoint(0,16000))
painter3.pointdistance=500
painter3.Straight(1000000)
painter3.TurningInterpolation(-400000)
painter3.TurningInterpolation(-400000)
painter3.Straight(1000000)
painter3.TurningInterpolation(400000)
painter3.TurningInterpolation(400000)

region1=painter3.Output_Region()

painter3.pointr=pya.DPoint(0,4000)
painter3.pointl=pya.DPoint(0,12000)

painter3.Straight(1000000)
painter3.TurningInterpolation(-400000)
painter3.TurningInterpolation(-400000)
painter3.Straight(1000000)
painter3.TurningInterpolation(400000)
painter3.TurningInterpolation(400000)

region2=painter3.Output_Region()

painter3.outputlist.append(region1-region2)
painter3.Output(cell2,layer1)

layer2 = layout.layer(1, 1)
painter2=paintlib.ObjectPainter()
painter2.DrawBorder()
painter2.DrawText("TEXT1",pya.DCplxTrans(100,45,False,-1000,-1000),cell,layer2,layout)

painter2.Output(cell,layer2)

#cell.shapes(layer1).insert(pya.Polygon.from_dpoly(pya.DPolygon(pts)))
layout.write(paintlib.IOsettings.Getfilename())#"[pythonout].gds"

#
'''
