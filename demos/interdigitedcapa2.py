# -*- coding: utf-8 -*-

#初始化
import pya
import paintlib180730 as paintlib
from imp import reload
reload(paintlib)
layout,top = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
layout.dbu = 0.001#设置单位长度为1nm
paintlib.IO.pointdistance=2000#设置腔的精度,转弯处相邻两点的距离
TBD=paintlib.TBD.init(686587)


for j in range(5):
       painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,290000),angle=90,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)

       def path1(painter):
           painter.Straight(100000)
       
           
       #painter3.Run(path1)    
       painter3.InterdigitedCapacitor(2*j+1,arg1=3000+82000*38.4/40.6,arg2=45000,arg3=31000,arg4=4000,arg5=3000,arg6=3000,arg7=2000) #38.4/40.6

#if number%2!=1:raise RuntimeError('number must be odd')  try except RuntimeError as:_

       layer1 = layout.layer(10, 0)#创建新层
       cell2 = layout.create_cell("Resonator1")#创建一个子cell
       top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
       painter3.Draw(cell2,layer1)#把画好的腔置入






       pts=[pya.Point(-2650000+j*500000,290000)]
       xx=pts[0].x+0
       yy=pts[0].y*0+377.5*1000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
       portbrushs=[
            paintlib.CavityBrush(pointc=pya.DPoint(xx,465000-82000*(1-38.4/40.6) ),angle=0,widout=8000,widin=4000,bgn_ext=0),
            paintlib.CavityBrush(pointc=pya.DPoint(xx,290000),angle=0,widout=8000,widin=4000,bgn_ext=0),
            #paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

       ]


       import simulation
       reload(simulation)
       Simulation=simulation.Simulation
        
       layerlist=[(10,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box) 5 to 7GHz
        #boxx=530000-22000,boxy=1607000+100000
       Simulation.create(
           name='intcapsn'+str(2*j+1),startfrequency=5,endfrequency=7,stepfrequency=2/300,
           layerlist=layerlist,boxx=150000,boxy=180000-5000-82000*(1-38.4/40.6),
           region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
           offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy-82000*(1-38.4/40.6)/2
           )

paintlib.IO.Show()

       



