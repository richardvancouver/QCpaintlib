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


def path3(painter,cavitylen=0, signn=1):#设置内轮廓路径
	lenthunit=397495.55921538756
	lenthentry=241371.66941154067
	lenthexit=150000
	frac=(cavitylen-lenthexit-lenthentry)/lenthunit
	print("sections: %s"%(frac))
	print("sections: %s"%( math.floor(frac) ))
	remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
	print("remainder: %s"%( remainder ))

	#entry
	length=0
	tinylenth=100000
	length+=painter.Straight(100000)
	length+=painter.Turning(-30000*signn)
	length+=painter.Straight(tinylenth)
	length+=painter.Turning(30000*signn)
	length+=painter.Turning(30000*signn)

	for i in range(9):
		#oldlength=length
		length+=painter.Straight(104500)#1
		length+=painter.Turning(-30000*signn)
		length+=painter.Turning(-30000*signn)
		length+=painter.Straight(104500)#2
		length+=painter.Turning(30000*signn)
		length+=painter.Turning(30000*signn)



	#length+=painter.Straight(150000+remainder)
	length+=painter.Straight(150000)  
	length+=painter.Turning(30000*signn)
	length+=painter.Straight(cavitylen-length)
	return length
        

#########resonator sec1############
for j in range(6):    
        wf=(5.65+0.05*j )*2*math.pi #p110 of sank: wf/2pi=6.75GHz
        epsilonr=11.4
        epsiloneff=(1+epsilonr)/2
        print("pi: %s" %(math.pi))
        print("sqrt: %s" %(math.sqrt(1.44)))
        cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        print("length1: %s"%(cavitylen))
        #画腔
        painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,290000),angle=90,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
        #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        tmp1=cavitylen
        signtmp1=1

        
        length=painter3.Run(lambda painter:path3(painter,cavitylen,1))
        import pathclass
        reload(pathclass)
        pat=pathclass.paths
        path=pat.getpath3(cavitylen=tmp1,signn=signtmp1)
        painter3.Run(path)
        
		#length=painter3.Run(pat)


		
        #print("length of resonator1 : %s"%(length))
        layer1 = layout.layer(10, 0)#创建新层
        cell2 = layout.create_cell("Resonator1")#创建一个子cell
        top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
        painter3.Draw(cell2,layer1)#把画好的腔置入

        painter3p5=paintlib.CavityPainter(pya.DPoint(-2840000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        #brush=painter3.brush

        painter4=paintlib.CavityPainter(pya.DPoint(-2840000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        def path(painter):
            painter.Straight(200000)
            
        painter4.Run(path)
        layer1 = layout.layer(10, 0)#创建新层
        cell3 = layout.create_cell("Trans1")#创建一个子cell
        top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        painter4.Draw(cell3,layer1)
        c4=painter4.Getcenterlineinfo()
        print("C4:%s" %c4)

#################qubits sec1############

        painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2c2.gds")

        pts=[pya.Point(-2750000+j*500000,140000)]
        xx=pts[0].x+11000
        yy=pts[0].y+850000-200000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        #portbrushs=[
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    #]
        painter1.DrawMark(top,pts,"qubit"+str(j))
#
        import simulation
        reload(simulation)
        Simulation=simulation.Simulation
        
        layerlist=[(10,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
        # Simulation.create(
            # name='Rqufine'+str(j),startfrequency=wf/(2*math.pi)-0.2,endfrequency=wf/(2*math.pi)+0.2,stepfrequency=0.4/300,
            # layerlist=layerlist,boxx=530000,boxy=1607000+100000,
            # region=None,brush=painter3p5.brush,transmissionlines=[c4],portbrushs=None,
            # offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
            # )
        
        
        #输出
        print(TBD.isFinish())
        paintlib.IO.Show()#输出到屏幕上
        #paintlib.IO.Write()#输出到文件中
        #



# ###################section 2#################
# for j in range(6):    
        # wf=(5.91+0.05*j )*2*math.pi #p110 of sank: wf/2pi=6.75GHz
        # epsilonr=11.4
        # epsiloneff=(1+epsilonr)/2
        # print("pi: %s" %(math.pi))
        # print("sqrt: %s" %(math.sqrt(1.44)))
        # cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        # print("length1: %s"%(cavitylen))
        # #画腔
        # painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000,290000),angle=90,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
        # #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        # #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
        # def path3(painter):#设置内轮廓路径
            # #painter.Turning(40000)
            # #painter.Straight(50000)
            # #painter.Turning(40000)
        
        
        
        
        
        
            # lenthunit=397495.55921538756
            # lenthentry=241371.66941154067
            # lenthexit=150000
            # frac=(cavitylen-lenthexit-lenthentry)/lenthunit
            # print("sections: %s"%(frac))
            # print("sections: %s"%( math.floor(frac) ))
            # remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
            # print("remainder: %s"%( remainder ))
        
            # #entry
            # length=0
            # tinylenth=100000
            # length+=painter.Straight(100000)
            # length+=painter.Turning(-30000*(-1))
            # length+=painter.Straight(tinylenth)
            # length+=painter.Turning(30000*(-1))
            # length+=painter.Turning(30000*(-1))
        
        
        
            # for i in range(9):
                # #oldlength=length
                # length+=painter.Straight(104500)#1
                # length+=painter.Turning(-30000*(-1))
                # length+=painter.Turning(-30000*(-1))
                # length+=painter.Straight(104500)#2
                # length+=painter.Turning(30000*(-1))
                # length+=painter.Turning(30000*(-1))
        
        
        
            # #length+=painter.Straight(150000+remainder)
            # length+=painter.Straight(150000)  
            # length+=painter.Turning(30000*(-1))
            # length+=painter.Straight(cavitylen-length)
            # return length
        
        
        # length=painter3.Run(path3)
        
        # #print("length of resonator1 : %s"%(length))
        # layer1 = layout.layer(10, 0)#创建新层
        # cell2 = layout.create_cell("Resonator1")#创建一个子cell
        # top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
        # painter3.Draw(cell2,layer1)#把画好的腔置入

        # painter3p5=paintlib.CavityPainter(pya.DPoint(150000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        # #brush=painter3.brush

        # painter4=paintlib.CavityPainter(pya.DPoint(150000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        # def path(painter):
            # painter.Straight(200000)
            
        # painter4.Run(path)
        # layer1 = layout.layer(10, 0)#创建新层
        # cell3 = layout.create_cell("Trans1")#创建一个子cell
        # top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        # painter4.Draw(cell3,layer1)
        # c4=painter4.Getcenterlineinfo()
        # print("C4:%s" %c4)

# #################qubits sec2############

        # painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cmirror2.gds")

        # pts=[pya.Point(250000+j*500000,140000)]
        # xx=pts[0].x+11000
        # yy=pts[0].y+850000-200000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        # #portbrushs=[
        # #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        # #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        # #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    # #]
        # painter1.DrawMark(top,pts,"qubit"+str(6+j))
# #
        # import simulation
        # reload(simulation)
        # Simulation=simulation.Simulation
        
        # layerlist=[(10,0)]
        # # box=pya.Box(-848740,-212112,40934,424224)
        # # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
        # Simulation.create(
            # name='Rqufine'+str(6+j),startfrequency=wf/(2*math.pi)-0.2,endfrequency=wf/(2*math.pi)+0.2,stepfrequency=0.4/300,
            # layerlist=layerlist,boxx=530000,boxy=1607000+100000,
            # region=None,brush=painter3p5.brush,transmissionlines=[c4],portbrushs=None,
            # offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
            # )
        
        
        # #输出
        # print(TBD.isFinish())
        # paintlib.IO.Show()#输出到屏幕上
        # #paintlib.IO.Write()#输出到文件中
        # #



# ###################section 3#################
# for j in range(6):    
        # wf=(6.17+0.05*j )*2*math.pi #p110 of sank: wf/2pi=6.75GHz
        # epsilonr=11.4
        # epsiloneff=(1+epsilonr)/2
        # print("pi: %s" %(math.pi))
        # print("sqrt: %s" %(math.sqrt(1.44)))
        # cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        # print("length1: %s"%(cavitylen))
        # #画腔
        # painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-290000),angle=270,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
        # #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        # #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
        # def path3(painter):#设置内轮廓路径
            # #painter.Turning(40000)
            # #painter.Straight(50000)
            # #painter.Turning(40000)
        
        
        
        
        
        
            # lenthunit=397495.55921538756
            # lenthentry=241371.66941154067
            # lenthexit=150000
            # frac=(cavitylen-lenthexit-lenthentry)/lenthunit
            # print("sections: %s"%(frac))
            # print("sections: %s"%( math.floor(frac) ))
            # remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
            # print("remainder: %s"%( remainder ))
        
            # #entry
            # length=0
            # tinylenth=100000
            # length+=painter.Straight(100000)
            # length+=painter.Turning(-30000*(-1))
            # length+=painter.Straight(tinylenth)
            # length+=painter.Turning(30000*(-1))
            # length+=painter.Turning(30000*(-1))
        
        
        
            # for i in range(9):
                # #oldlength=length
                # length+=painter.Straight(104500)#1
                # length+=painter.Turning(-30000*(-1))
                # length+=painter.Turning(-30000*(-1))
                # length+=painter.Straight(104500)#2
                # length+=painter.Turning(30000*(-1))
                # length+=painter.Turning(30000*(-1))
        
        
        
            # #length+=painter.Straight(150000+remainder)
            # length+=painter.Straight(150000)  
            # length+=painter.Turning(30000*(-1))
            # length+=painter.Straight(cavitylen-length)
            # return length
        
        
        # length=painter3.Run(path3)
        
        # #print("length of resonator1 : %s"%(length))
        # layer1 = layout.layer(10, 0)#创建新层
        # cell2 = layout.create_cell("Resonator1")#创建一个子cell
        # top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
        # painter3.Draw(cell2,layer1)#把画好的腔置入

        # painter3p5=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        # #brush=painter3.brush

        # painter4=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        # def path(painter):
            # painter.Straight(200000)
            
        # painter4.Run(path)
        # layer1 = layout.layer(10, 0)#创建新层
        # cell3 = layout.create_cell("Trans1")#创建一个子cell
        # top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        # painter4.Draw(cell3,layer1)
        # c4=painter4.Getcenterlineinfo()
        # print("C4:%s" %c4)

# #################qubits sec3############

        # painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cm32.gds")

        # pts=[pya.Point(-2750000+j*500000,-140000-14000)]
        # xx=pts[0].x+11000
        # yy=pts[0].y-850000+200000-45.5*1000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        # #portbrushs=[
        # #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        # #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        # #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    # #]
        # painter1.DrawMark(top,pts,"qubit"+str(12+j))
# #
        # import simulation
        # reload(simulation)
        # Simulation=simulation.Simulation
        
        # layerlist=[(10,0)]
        # # box=pya.Box(-848740,-212112,40934,424224)
        # # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
        # Simulation.create(
            # name='Rqufine'+str(12+j),startfrequency=wf/(2*math.pi)-0.2,endfrequency=wf/(2*math.pi)+0.2,stepfrequency=0.4/300,
            # layerlist=layerlist,boxx=530000,boxy=1607000+100000,
            # region=None,brush=painter3p5.brush,transmissionlines=None,portbrushs=None,
            # offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
            # )
        
        # #[c4]
        # #输出
        # print(TBD.isFinish())
        # paintlib.IO.Show()#输出到屏幕上
        # #paintlib.IO.Write()#输出到文件中
        # #





# ###################section 4#################
# for j in range(6):    
        # wf=(6.43+0.05*j )*2*math.pi #p110 of sank: wf/2pi=6.75GHz
        # epsilonr=11.4
        # epsiloneff=(1+epsilonr)/2
        # print("pi: %s" %(math.pi))
        # print("sqrt: %s" %(math.sqrt(1.44)))
        # cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        # print("length1: %s"%(cavitylen))
        # #画腔
        # painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-290000),angle=270,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
        # #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        # #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
        # def path3(painter):#设置内轮廓路径
            # #painter.Turning(40000)
            # #painter.Straight(50000)
            # #painter.Turning(40000)
        
        
        
        
        
        
            # lenthunit=397495.55921538756
            # lenthentry=241371.66941154067
            # lenthexit=150000
            # frac=(cavitylen-lenthexit-lenthentry)/lenthunit
            # print("sections: %s"%(frac))
            # print("sections: %s"%( math.floor(frac) ))
            # remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
            # print("remainder: %s"%( remainder ))
        
            # #entry
            # length=0
            # tinylenth=100000
            # length+=painter.Straight(100000)
            # length+=painter.Turning(-30000*(1))
            # length+=painter.Straight(tinylenth)
            # length+=painter.Turning(30000*(1))
            # length+=painter.Turning(30000*(1))
        
        
        
            # for i in range(9):
                # #oldlength=length
                # length+=painter.Straight(104500)#1
                # length+=painter.Turning(-30000*(1))
                # length+=painter.Turning(-30000*(1))
                # length+=painter.Straight(104500)#2
                # length+=painter.Turning(30000*(1))
                # length+=painter.Turning(30000*(1))
        
        
        
            # #length+=painter.Straight(150000+remainder)
            # length+=painter.Straight(150000)  
            # length+=painter.Turning(30000*(1))
            # length+=painter.Straight(cavitylen-length)
            # return length
        
        
        # length=painter3.Run(path3)
        
        # #print("length of resonator1 : %s"%(length))
        # layer1 = layout.layer(10, 0)#创建新层
        # cell2 = layout.create_cell("Resonator1")#创建一个子cell
        # top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
        # painter3.Draw(cell2,layer1)#把画好的腔置入

        # painter3p5=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        # #brush=painter3.brush

        # painter4=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        # def path(painter):
            # painter.Straight(200000)
            
        # painter4.Run(path)
        # layer1 = layout.layer(10, 0)#创建新层
        # cell3 = layout.create_cell("Trans1")#创建一个子cell
        # top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        # painter4.Draw(cell3,layer1)
        # c4=painter4.Getcenterlineinfo()
        # print("C4:%s" %c4)

# #################qubits sec4############

        # painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cmirrorb2.gds")

        # pts=[pya.Point(250000+j*500000,-140000-14000)]
        # xx=pts[0].x+11000
        # yy=pts[0].y-850000+200000-45.5*1000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        # #portbrushs=[
        # #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        # #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        # #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    # #]
        # painter1.DrawMark(top,pts,"qubit"+str(18+j))
# #
        # import simulation
        # reload(simulation)
        # Simulation=simulation.Simulation
        
        # layerlist=[(10,0)]
        # # box=pya.Box(-848740,-212112,40934,424224)
        # # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
        # Simulation.create(
            # name='Rqufine'+str(18+j),startfrequency=wf/(2*math.pi)-0.2,endfrequency=wf/(2*math.pi)+0.2,stepfrequency=0.4/300,
            # layerlist=layerlist,boxx=530000,boxy=1607000+100000,
            # region=None,brush=painter3p5.brush,transmissionlines=[c4],portbrushs=None,
            # offsetx=0,offsety=0,deltaangle=0,absx=xx,absy=yy
            # )
        
        
        # #输出
        # print(TBD.isFinish())
        # paintlib.IO.Show()#输出到屏幕上
        #paintlib.IO.Write()#输出到文件中
        #








