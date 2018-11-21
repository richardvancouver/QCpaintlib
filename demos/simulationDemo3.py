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



for j in range(6):    
        wf=(5.85+0.05*j )*2*math.pi #p110 of sank: wf/2pi=6.75GHz
        epsilonr=11.4
        epsiloneff=(1+epsilonr)/2
        print("pi: %s" %(math.pi))
        print("sqrt: %s" %(math.sqrt(1.44)))
        cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        print("length1: %s"%(cavitylen))
        #画腔
        painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,290000-5000),angle=90,widout=8000,widin=4000,bgn_ext=5000,end_ext=0000)
        #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
        def path3(painter):#设置内轮廓路径
            #painter.Turning(40000)
            #painter.Straight(50000)
            #painter.Turning(40000)
        
        
        
        
        
        
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
            length+=painter.Turning(-30000)
            length+=painter.Straight(tinylenth)
            length+=painter.Turning(30000)
            length+=painter.Turning(30000)
        
        
        
            for i in range(9):
                #oldlength=length
                length+=painter.Straight(104500)#1
                length+=painter.Turning(-30000)
                length+=painter.Turning(-30000)
                length+=painter.Straight(104500)#2
                length+=painter.Turning(30000)
                length+=painter.Turning(30000)
        
        
        
            #length+=painter.Straight(150000+remainder)
            length+=painter.Straight(150000)  
            length+=painter.Turning(30000)
            length+=painter.Straight(cavitylen-length)
            return length
        
        
        length=painter3.Run(path3)
        
        #print("length of resonator1 : %s"%(length))
        layer1 = layout.layer(10, 10)#创建新层
        cell2 = layout.create_cell("Resonator1")#创建一个子cell
        top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
        painter3.Draw(cell2,layer1)#把画好的腔置入

        painter3p5=paintlib.CavityPainter(pya.DPoint(-2840000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        #brush=painter3.brush

        painter4=paintlib.CavityPainter(pya.DPoint(-2840000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        def path(painter):
            painter.Straight(200000)
            
        painter4.Run(path)
        layer1 = layout.layer(10, 10)#创建新层
        cell3 = layout.create_cell("Trans1")#创建一个子cell
        top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        painter4.Draw(cell3,layer1)
        c4=painter4.Getcenterlineinfo()
        print("C4:%s" %c4)


#
        import simulation
        reload(simulation)
        Simulation=simulation.Simulation
        
        layerlist=[(10,10)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
        Simulation.create(
            name='Restest'+str(j),startfrequency=5.85+0.05*j-0.05,endfrequency=5.85+0.05*j+0.05,stepfrequency=0.1/300,
            layerlist=layerlist,boxx=530000,boxy=1360000,
            region=painter3.region,brush=painter3p5.brush,transmissionlines=[c4],portbrushs=None,
            offsetx=0,offsety=0,deltaangle=0,absx=None,absy=None
            )
        
        
        #输出
        print(TBD.isFinish())
        paintlib.IO.Show()#输出到屏幕上
        #paintlib.IO.Write()#输出到文件中
        #






###################section 2#################

for j in range(6):    
        wf=(6.15+0.05*j )*2*math.pi #p110 of sank: wf/2pi=6.75GHz
        epsilonr=11.4
        epsiloneff=(1+epsilonr)/2
        print("pi: %s" %(math.pi))
        print("sqrt: %s" %(math.sqrt(1.44)))
        cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        print("length1: %s"%(cavitylen))
        #画腔
        painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000,290000-5000),angle=90,widout=8000,widin=4000,bgn_ext=5000,end_ext=0000)
        #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
        def path3(painter):#设置内轮廓路径
            #painter.Turning(40000)
            #painter.Straight(50000)
            #painter.Turning(40000)
        
        
        
        
        
        
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
            length+=painter.Turning(-30000*(-1))
            length+=painter.Straight(tinylenth)
            length+=painter.Turning(30000*(-1))
            length+=painter.Turning(30000*(-1))
        
        
        
            for i in range(9):
                #oldlength=length
                length+=painter.Straight(104500)#1
                length+=painter.Turning(-30000*(-1))
                length+=painter.Turning(-30000*(-1))
                length+=painter.Straight(104500)#2
                length+=painter.Turning(30000*(-1))
                length+=painter.Turning(30000*(-1))
        
        
        
            #length+=painter.Straight(150000+remainder)
            length+=painter.Straight(150000)  
            length+=painter.Turning(30000*(-1))
            length+=painter.Straight(cavitylen-length)
            return length
        
        
        length=painter3.Run(path3)
        
        #print("length of resonator1 : %s"%(length))
        layer1 = layout.layer(10, 10)#创建新层
        cell2 = layout.create_cell("Resonator1")#创建一个子cell
        top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
        painter3.Draw(cell2,layer1)#把画好的腔置入

        painter3p5=paintlib.CavityPainter(pya.DPoint(150000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        #brush=painter3.brush

        painter4=paintlib.CavityPainter(pya.DPoint(150000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        def path(painter):
            painter.Straight(200000)
            
        painter4.Run(path)
        layer1 = layout.layer(10, 10)#创建新层
        cell3 = layout.create_cell("Trans1")#创建一个子cell
        top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        painter4.Draw(cell3,layer1)
        c4=painter4.Getcenterlineinfo()
        print("C4:%s" %c4)


#
        import simulation
        reload(simulation)
        Simulation=simulation.Simulation
        
        layerlist=[(10,10)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
        Simulation.create(
            name='Restest'+str(j+6),startfrequency=6.15+0.05*j-0.05,endfrequency=6.15+0.05*j+0.05,stepfrequency=0.1/300,
            layerlist=layerlist,boxx=530000,boxy=1360000,
            region=painter3.region,brush=painter3p5.brush,transmissionlines=[c4],portbrushs=None,
            offsetx=0,offsety=0,deltaangle=0,absx=None,absy=None
            )
        
        
        #输出
        print(TBD.isFinish())
        paintlib.IO.Show()#输出到屏幕上


###################section 3#################

for j in range(6):    
        wf=(6.45+0.05*j )*2*math.pi #p110 of sank: wf/2pi=6.75GHz
        epsilonr=11.4
        epsiloneff=(1+epsilonr)/2
        print("pi: %s" %(math.pi))
        print("sqrt: %s" %(math.sqrt(1.44)))
        cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        print("length1: %s"%(cavitylen))
        #画腔
        painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-290000+5000),angle=270,widout=8000,widin=4000,bgn_ext=5000,end_ext=0000)
        #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
        def path3(painter):#设置内轮廓路径
            #painter.Turning(40000)
            #painter.Straight(50000)
            #painter.Turning(40000)
        
        
        
        
        
        
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
            length+=painter.Turning(-30000*(-1))
            length+=painter.Straight(tinylenth)
            length+=painter.Turning(30000*(-1))
            length+=painter.Turning(30000*(-1))
        
        
        
            for i in range(9):
                #oldlength=length
                length+=painter.Straight(104500)#1
                length+=painter.Turning(-30000*(-1))
                length+=painter.Turning(-30000*(-1))
                length+=painter.Straight(104500)#2
                length+=painter.Turning(30000*(-1))
                length+=painter.Turning(30000*(-1))
        
        
        
            #length+=painter.Straight(150000+remainder)
            length+=painter.Straight(150000)  
            length+=painter.Turning(30000*(-1))
            length+=painter.Straight(cavitylen-length)
            return length
        
        
        length=painter3.Run(path3)
        
        #print("length of resonator1 : %s"%(length))
        layer1 = layout.layer(10, 10)#创建新层
        cell2 = layout.create_cell("Resonator1")#创建一个子cell
        top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
        painter3.Draw(cell2,layer1)#把画好的腔置入

        painter3p5=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        #brush=painter3.brush

        painter4=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        def path(painter):
            painter.Straight(200000)
            
        painter4.Run(path)
        layer1 = layout.layer(10, 10)#创建新层
        cell3 = layout.create_cell("Trans1")#创建一个子cell
        top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        painter4.Draw(cell3,layer1)
        c4=painter4.Getcenterlineinfo()
        print("C4:%s" %c4)


#
        import simulation
        reload(simulation)
        Simulation=simulation.Simulation
        
        layerlist=[(10,10)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
        Simulation.create(
            name='Restest'+str(j+12),startfrequency=6.45+0.05*j-0.05,endfrequency=6.45+0.05*j+0.05,stepfrequency=0.1/300,
            layerlist=layerlist,boxx=530000,boxy=1360000,
            region=painter3.region,brush=painter3p5.brush,transmissionlines=[c4],portbrushs=None,
            offsetx=0,offsety=0,deltaangle=0,absx=None,absy=None
            )
        
        
        #输出
        print(TBD.isFinish())
        paintlib.IO.Show()#输出到屏幕上


###################section 4#################

for j in range(6):    
        wf=(6.75+0.05*j )*2*math.pi #p110 of sank: wf/2pi=6.75GHz
        epsilonr=11.4
        epsiloneff=(1+epsilonr)/2
        print("pi: %s" %(math.pi))
        print("sqrt: %s" %(math.sqrt(1.44)))
        cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        print("length1: %s"%(cavitylen))
        #画腔
        painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-290000+5000),angle=270,widout=8000,widin=4000,bgn_ext=5000,end_ext=0000)
        #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
        def path3(painter):#设置内轮廓路径
            #painter.Turning(40000)
            #painter.Straight(50000)
            #painter.Turning(40000)
        
        
        
        
        
        
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
            length+=painter.Turning(-30000*(1))
            length+=painter.Straight(tinylenth)
            length+=painter.Turning(30000*(1))
            length+=painter.Turning(30000*(1))
        
        
        
            for i in range(9):
                #oldlength=length
                length+=painter.Straight(104500)#1
                length+=painter.Turning(-30000*(1))
                length+=painter.Turning(-30000*(1))
                length+=painter.Straight(104500)#2
                length+=painter.Turning(30000*(1))
                length+=painter.Turning(30000*(1))
        
        
        
            #length+=painter.Straight(150000+remainder)
            length+=painter.Straight(150000)  
            length+=painter.Turning(30000*(1))
            length+=painter.Straight(cavitylen-length)
            return length
        
        
        length=painter3.Run(path3)
        
        #print("length of resonator1 : %s"%(length))
        layer1 = layout.layer(10, 10)#创建新层
        cell2 = layout.create_cell("Resonator1")#创建一个子cell
        top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
        painter3.Draw(cell2,layer1)#把画好的腔置入

        painter3p5=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        #brush=painter3.brush

        painter4=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        def path(painter):
            painter.Straight(200000)
            
        painter4.Run(path)
        layer1 = layout.layer(10, 10)#创建新层
        cell3 = layout.create_cell("Trans1")#创建一个子cell
        top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        painter4.Draw(cell3,layer1)
        c4=painter4.Getcenterlineinfo()
        print("C4:%s" %c4)


#
        import simulation
        reload(simulation)
        Simulation=simulation.Simulation
        
        layerlist=[(10,10)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
        Simulation.create(
            name='Restest'+str(j+18),startfrequency=6.75+0.05*j-0.05,endfrequency=6.75+0.05*j+0.05,stepfrequency=0.1/300,
            layerlist=layerlist,boxx=530000,boxy=1360000,
            region=painter3.region,brush=painter3p5.brush,transmissionlines=[c4],portbrushs=None,
            offsetx=0,offsety=0,deltaangle=0,absx=None,absy=None
            )
        
        
        #输出
        print(TBD.isFinish())
        paintlib.IO.Show()#输出到屏幕上
