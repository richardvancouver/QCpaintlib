# -*- coding: utf-8 -*-

#初始化
import pya
import paintlib180730c as paintlib
from imp import reload
reload(paintlib)
layout,top = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
layout.dbu = 0.001#设置单位长度为1nm
paintlib.IO.pointdistance=2000#设置腔的精度,转弯处相邻两点的距离
TBD=paintlib.TBD.init(686587)


pts=[pya.Point(40000,-100000)]
xx=pts[0].x
yy=pts[0].y #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
portbrushs=[
    paintlib.CavityBrush(pointc=pya.DPoint(xx,yy-110000),angle=0,widout=8000,widin=4000,bgn_ext=0),
    paintlib.CavityBrush(pointc=pya.DPoint(xx+73000,yy),angle=0,widout=8000,widin=4000,bgn_ext=0),
    #paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

]


import simulationtrilayerc
reload(simulationtrilayerc)
Simulation=simulationtrilayerc.Simulation
        
layerlist=[(2,0)]
layerlistvia1=[(12,0)]
layerlistbr1=[(6,0)]
layerlistbk1=[(8,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box) 5 to 7GHz
        #boxx=530000-22000,boxy=1607000+100000
#       Simulation.create(
#           name='tttriof'+str(j),startfrequency=freqs1pk[j]-0.015,endfrequency=freqs1pk[j]+0.015,stepfrequency=2/300,
#          layerlist=layerlist,layerlistvia=layerlistvia1,layerlistbr=layerlistbr1,boxx=530000-22000,boxy=1750000*2-300000 -1500000 -24000,
#           region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
#           offsetx=0,offsety=0,deltaangle=0,absx=xx-22000/2,absy=yy+60000+900000-300000/2 -1500000/2+4000 +24000/2
#           )



######up filter#######
Simulation.create(
   name='testbrick',startfrequency=4,endfrequency=8,stepfrequency=2/300,
   layerlist=layerlist,layerlistvia=layerlistvia1,layerlistbk=layerlistbk1,layerlistbr=layerlistbr1,boxx=142000,boxy=225000,
   region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
   offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
   )

#############
