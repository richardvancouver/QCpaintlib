# -*- coding: utf-8 -*-

#初始化
import pya
import paintlib180730 as paintlib
from imp import reload
reload(paintlib)
layout,top = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
layout.dbu = 0.001#设置单位长度为1nm
paintlib.IO.pointdistance=2000#设置腔的精度,转弯处相邻两点的距离
TBD=paintlib.TBD.init(6876587)



#画Mark
#painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2.gds")
#pts=[pya.Point(-2750000,140000),pya.Point(-2250000,140000),pya.Point(-1750000,140000)]
#painter1.DrawMark(top,pts,"qubit")
####sec1
painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2c.gds")
for j in range(6):
    pts=[pya.Point(-2750000+j*500000,140000)]
    xx=pts[0].x+11000
    yy=pts[0].y+7000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
    portbrushs=[
        paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    ]
    painter1.DrawMark(top,pts,"qubit"+str(j))
#end

    import simulation
    reload(simulation)
    Simulation=simulation.Simulation
        
    layerlist=[(10,0)]
    # box=pya.Box(-848740,-212112,40934,424224)
    # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
    Simulation.create(
        name='Qutest'+str(j),startfrequency=5.85+0.05*j-0.05,endfrequency=5.85+0.05*j+0.05,stepfrequency=0.1/300,
        layerlist=layerlist,boxx=530000,boxy=286000,
        region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
        offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
        )
        
        
        #输出
    #print(TBD.isFinish())
    paintlib.IO.Show()#输出到屏幕上

#pts=[pya.Point(-2750000,140000)]
#painter1.DrawMark(top,pts,"qubit")
#pts=[pya.Point(-2250000,140000)]
#painter1.DrawMark(top,pts,"qubit")
#pts=[pya.Point(-1750000,140000)]
#painter1.DrawMark(top,pts,"qubit")

###sec2
painter2=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cmirror.gds")
for j in range(6):
    pts=[pya.Point(250000+j*500000,140000)]
    xx=pts[0].x+11000
    yy=pts[0].y+7000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
    portbrushs=[
        paintlib.CavityBrush(pointc=pya.DPoint(xx+116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        paintlib.CavityBrush(pointc=pya.DPoint(xx-100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    ]
    painter2.DrawMark(top,pts,"qubit"+str(6+j))
#end

    import simulation
    reload(simulation)
    Simulation=simulation.Simulation
        
    layerlist=[(10,0)]
    # box=pya.Box(-848740,-212112,40934,424224)
    # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
    Simulation.create(
        name='Qutest'+str(6+j),startfrequency=5.85+0.05*j-0.05,endfrequency=5.85+0.05*j+0.05,stepfrequency=0.1/300,
        layerlist=layerlist,boxx=530000,boxy=286000,
        region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
        offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
        )
        
        
        #输出
    #print(TBD.isFinish())
    paintlib.IO.Show()#输出到屏幕上


#####sec3
painter3=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cm3.gds")
for j in range(6):
    pts=[pya.Point(-2750000+j*500000,-140000-14000)]
    xx=pts[0].x+11000
    yy=pts[0].y+7000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
    portbrushs=[
        paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy-150000+7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy-150000+7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy+136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    ]
    painter3.DrawMark(top,pts,"qubit"+str(12+j))
#end

    import simulation
    reload(simulation)
    Simulation=simulation.Simulation
        
    layerlist=[(10,0)]
    # box=pya.Box(-848740,-212112,40934,424224)
    # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
    Simulation.create(
        name='Qutest'+str(12+j),startfrequency=5.85+0.05*j-0.05,endfrequency=5.85+0.05*j+0.05,stepfrequency=0.1/300,
        layerlist=layerlist,boxx=530000,boxy=286000,
        region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
        offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
        )
        
        
        #输出
    #print(TBD.isFinish())
    paintlib.IO.Show()#输出到屏幕上









#######sec4#
#painter4=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cm4.gds")
painter4=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cmirrorb.gds")

for j in range(6):
    pts=[pya.Point(250000+j*500000,-140000-14000)]
    xx=pts[0].x+11000
    yy=pts[0].y+7000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
    portbrushs=[
        paintlib.CavityBrush(pointc=pya.DPoint(xx+116000,yy-150000+7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        paintlib.CavityBrush(pointc=pya.DPoint(xx-100000,yy-150000+7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy+136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    ]
    painter4.DrawMark(top,pts,"qubit"+str(18+j))
#end

    import simulation
    reload(simulation)
    Simulation=simulation.Simulation
        
    layerlist=[(10,0)]
    # box=pya.Box(-848740,-212112,40934,424224)
    # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
    Simulation.create(
        name='Qutest'+str(18+j),startfrequency=5.85+0.05*j-0.05,endfrequency=5.85+0.05*j+0.05,stepfrequency=0.1/300,
        layerlist=layerlist,boxx=530000,boxy=286000,
        region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
        offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
        )
        
        
        #输出
    #print(TBD.isFinish())
    paintlib.IO.Show()#输出到屏幕上




#输出
#print(TBD.isFinish())
paintlib.IO.Show()#输出到屏幕上
#paintlib.IO.Write()#输出到文件中
#

