# -*- coding: utf-8 -*-

#初始化
import pya
import paintlib180804 as paintlib #paintlib180730 paintlib180804
from imp import reload
reload(paintlib)
layout,top = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
layout.dbu = 0.001#设置单位长度为1nm
paintlib.IO.pointdistance=2000#设置腔的精度,转弯处相邻两点的距离
TBD=paintlib.TBD.init(686587)

CgL=80000
dCkx=0#5000 #Ckx=2um+dCkx
Ckl=10000

layer1 = layout.layer(10, 0)#创建新层
cell2 = layout.create_cell("Resonator1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
#########resonator sec1############
painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2c2.gds")

for j in range(6):    


#################qubits sec1############


        pts=[pya.Point(-2750000+j*500000,140000)]
        xx=pts[0].x+11000
        yy=pts[0].y+850000-200000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        #portbrushs=[
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    #]
        painter1.DrawMark(top,pts,"qubit"+str(j))
        
       # the claw, Cg
        cellclaw = layout.create_cell("Claw")#创建一个子cell
        top.insert(pya.CellInstArray(cellclaw.cell_index(),pya.Trans()))

        painter7=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,271000+2500),angle=270,widout=48000,widin=16000,bgn_ext=0,end_ext=0)
        painter7.Connection(clength=CgL,cwid=53000,widin=4000,widout=145000,linewid=5000,slength1=5000,slength2=17000,reverse=False)
        painter7.Draw(cellclaw,layer1)
#widin=16000, widout=114000, linewid=5000, slength1=16000, slength2=16000, clength=30000, cwid=54000,y=0,angle=0		
		#cut out the region for simulating the resonator
        import simulation
        reload(simulation)
        Simulation=simulation.Simulation
        
        layerlist=[(10,0)]
    # box=pya.Box(-848740,-212112,40934,424224)
    # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
        Simulation.create(
            name='Qutestgetb'+str(j),startfrequency=5.85+0.05*j-0.05,endfrequency=5.85+0.05*j+0.05,stepfrequency=0.1/300,
            layerlist=layerlist,boxx=530000,boxy=286000,
            region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
            offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
            )
        
        
        # #输出
        # print(TBD.isFinish())
        # paintlib.IO.Show()#输出到屏幕上
        #paintlib.IO.Write()#输出到文件中
        #

##
#BP Filter

####cut out the Sank filter region###

#输出
#print(TBD.isFinish())
paintlib.IO.Show()#输出到屏幕上
#paintlib.IO.Write()#输出到文件中


###################section 2#################
painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cmirror2.gds")

for j in range(6):    

#################qubits sec2############


        pts=[pya.Point(250000+j*500000,140000)]
        xx=pts[0].x+11000
        yy=pts[0].y+850000-200000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        #portbrushs=[
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    #]
        painter1.DrawMark(top,pts,"qubit"+str(6+j))
#       # the claw, Cg
        cellclaw = layout.create_cell("Claw")#创建一个子cell
        top.insert(pya.CellInstArray(cellclaw.cell_index(),pya.Trans()))

        painter7=paintlib.CavityPainter(pya.DPoint(150000+j*500000,271000+2500),angle=270,widout=48000,widin=16000,bgn_ext=0,end_ext=0)
        painter7.Connection(clength=CgL,cwid=53000,widin=4000,widout=145000,linewid=5000,slength1=5000,slength2=17000,reverse=False)
        painter7.Draw(cellclaw,layer1)
        
        import simulation
        reload(simulation)
        Simulation=simulation.Simulation
            
        layerlist=[(10,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
            
        Simulation.create(
            name='Qutestgetb'+str(6+j),startfrequency=5.85+0.05*j-0.05,endfrequency=5.85+0.05*j+0.05,stepfrequency=0.1/300,
            layerlist=layerlist,boxx=530000,boxy=286000,
            region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
            offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
            )

##
#BP Filter


#输出
#print(TBD.isFinish())
paintlib.IO.Show()#输出到屏幕上
#paintlib.IO.Write()#输出到文件中

###################section 3#################
painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cm32.gds")

for j in range(6):    


#################qubits sec3############


        pts=[pya.Point(-2750000+j*500000,-140000-14000)]
        xx=pts[0].x+11000
        yy=pts[0].y-850000+200000-45.5*1000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        #portbrushs=[
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    #]
        painter1.DrawMark(top,pts,"qubit"+str(12+j))
#       # the claw, Cg
        cellclaw = layout.create_cell("Claw")#创建一个子cell
        top.insert(pya.CellInstArray(cellclaw.cell_index(),pya.Trans()))

        painter7=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-(271000+2500)),angle=90,widout=48000,widin=16000,bgn_ext=0,end_ext=0)
        painter7.Connection(clength=CgL,cwid=53000,widin=4000,widout=145000,linewid=5000,slength1=5000,slength2=17000,reverse=False)
        painter7.Draw(cellclaw,layer1)
        import simulation
        reload(simulation)
        Simulation=simulation.Simulation
            
        layerlist=[(10,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
            
        Simulation.create(
            name='Qutestgetb'+str(12+j),startfrequency=5.85+0.05*j-0.05,endfrequency=5.85+0.05*j+0.05,stepfrequency=0.1/300,
            layerlist=layerlist,boxx=530000,boxy=286000,
            region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
            offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
            )

##
#BP Filter

#输出
#print(TBD.isFinish())
paintlib.IO.Show()#输出到屏幕上
#paintlib.IO.Write()#输出到文件中

###################section 4#################
painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cmirrorb2.gds")

for j in range(6):    


#################qubits sec4############


        pts=[pya.Point(250000+j*500000,-140000-14000)]
        xx=pts[0].x+11000
        yy=pts[0].y-850000+200000-45.5*1000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        #portbrushs=[
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    #]
        painter1.DrawMark(top,pts,"qubit"+str(18+j))
#       # the claw, Cg
        cellclaw = layout.create_cell("Claw")#创建一个子cell
        top.insert(pya.CellInstArray(cellclaw.cell_index(),pya.Trans()))

        painter7=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-(271000+2500)),angle=90,widout=48000,widin=16000,bgn_ext=0,end_ext=0)
        painter7.Connection(clength=CgL,cwid=53000,widin=4000,widout=145000,linewid=5000,slength1=5000,slength2=17000,reverse=False)
        painter7.Draw(cellclaw,layer1)

        import simulation
        reload(simulation)
        Simulation=simulation.Simulation
            
        layerlist=[(10,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
            
        Simulation.create(
            name='Qutestgetb'+str(18+j),startfrequency=5.85+0.05*j-0.05,endfrequency=5.85+0.05*j+0.05,stepfrequency=0.1/300,
            layerlist=layerlist,boxx=530000,boxy=286000,
            region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
            offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
            )
##
#BP Filter

#输出
#print(TBD.isFinish())
paintlib.IO.Show()#输出到屏幕上
#paintlib.IO.Write()#输出到文件中




