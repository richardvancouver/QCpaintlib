# -*- coding: utf-8 -*-
#KLayout 0.24.8
#python 3.4
import paintlib
import pya
from math import cos,sin,pi
Interactive=paintlib.Interactive
CavityPainter=paintlib.CavityPainter
IO=paintlib.IO

with open(IO.path+'/matlabtpl.m') as fid:
    _matlabtpl=fid.read()

class Simulation:
    matlabfiletpl=_matlabtpl

    @staticmethod
    def _get_region_cell_port_from_resonator_and_transmissionline(region,brush,layerlist,boxx,boxy,deltaangle=0):
        '''先把图像逆时针转deltaangle角度后沿着平直截取'''
        painter=CavityPainter(brush) #brush不能绘图，需要生成一个painter才能绘图
        painter.Run(lambda painter:painter._Straight(10)+painter._Straight(-10)) #画一个10nm size的小图形以此作为上边沿，bbox()的作用是四周划线靠拢直到碰到图形，从而确定边界
        _pb=[region.bbox(),painter.Output_Region().bbox()] #合并两个区域，只包含读取腔的盒子和 包含读取腔和10nm小物件的区域
        _pbr=pya.Region() #合并区域吧
        for ii in _pb:_pbr.insert(ii)
        pc=_pbr.bbox().center()     #找到区域中心，大区域中心。只找读取腔所在的盒子的中心可能会导致下面的留白不均匀
        
        # tr1=pya.DCplxTrans(1,-deltaangle,False,-pc.x,-pc.y)

        box=pya.Box(pc.x-boxx/2,pc.y-boxy/2,pc.x+boxx/2,pc.y+boxy/2)# .transformed(pya.ICplxTrans.from_dtrans(tr1)) #制造等距离的留白
        outregion,inregion=Interactive.cut(layerlist=layerlist,layermod='in',box=box,mergeanddraw=False) #割出这个大区域出来
        painter.Run(lambda painter:painter._Straight(-boxx-boxy)) #画横贯整个box宽度的传输线
        painter.Run(lambda painter:painter.Straight(2*boxx+2*boxy)) #画横贯整个box宽度的传输线
        inregion=inregion+painter.Output_Region()

        #计算端口
        br=painter.brush
        pt=pya.DPoint(br.centerx,br.centery)
        angle=br.angle
        edge=pya.DEdge(pt.x,pt.y,pt.x-(2*boxx+2*boxy)*cos(angle/180*pi),pt.y-(2*boxx+2*boxy)*sin(angle/180*pi)) #画横贯传输线的水平线
        edges=[ #左,上,右,下
            pya.DEdge(pc.x-boxx/2,pc.y-boxy/2,pc.x-boxx/2,pc.y+boxy/2),
            pya.DEdge(pc.x-boxx/2,pc.y+boxy/2,pc.x+boxx/2,pc.y+boxy/2),
            pya.DEdge(pc.x+boxx/2,pc.y+boxy/2,pc.x+boxx/2,pc.y-boxy/2),
            pya.DEdge(pc.x+boxx/2,pc.y-boxy/2,pc.x-boxx/2,pc.y-boxy/2)
        ]  #盒子的四个边
        ports=[ee.crossing_point(edge) for ee in edges if ee.crossed_by(edge)] #画横贯传输线的水平线，找到交点，交点就是ports
        
        final_region,cell,tr=Interactive._merge_and_draw(outregion,inregion)  #合并传输线和盒子

        ports=[[pt.x-tr[0],pt.y-tr[1]] for pt in ports] #把端口坐标设成以盒子中心为中心
        return final_region,cell,ports
    
    @staticmethod
    def _format_region_into_matlab_code(region,name,prefix=''):
        output=[]
        def pushln(ss):
            output.append(prefix+ss+'\n')

        vname=name+'_xy'
        pushln(vname+'={};')
        for polygon in region.each():
            xx=[]
            yy=[]
            for pt in polygon.to_simple_polygon().each_point():
                xx.append(str(pt.x))
                yy.append(str(pt.y))
            pushln('xx_=['+','.join(xx)+'];')
            pushln('yy_=['+','.join(yy)+'];')
            pushln(vname+'{end+1}={xx_,yy_};')
        
        return output

    @staticmethod #static method不用设self变量
    def resonator_transmissionline(region,brush,layerlist,boxx,boxy,name,startfrequency,endfrequency,stepfrequency,deltaangle=0):
        '''
        frequency单位GHz
        '''
        final_region,cell,ports=Simulation._get_region_cell_port_from_resonator_and_transmissionline(
            region=region,brush=brush,layerlist=layerlist,boxx=boxx,boxy=boxy,deltaangle=deltaangle
        )
        cell.name=name
        prefix=''
        output=Simulation._format_region_into_matlab_code(region=final_region,name=name,prefix=prefix)
        def pushln(ss):
            output.append(prefix+ss+'\n')
        pushln(name+'_ports='+str(ports)+';')
        pushln(name+'_boxsize='+str([boxx,boxy])+';')
        pushln(name+'_sweep='+str([startfrequency,endfrequency,stepfrequency])+';')
        pushln('project_name_=\''+name+'\';')
        pushln(Simulation.matlabfiletpl.replace('\n','\n'+prefix).replace('TBD_projectname',name))
        ss=''.join(output)
        with open('sonnet_'+name+'.m','w') as fid:
            fid.write(ss)
            print('sonnet_'+name+'.m')