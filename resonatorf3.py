# Enter your Python code here



import pya
import paintlib
from imp import reload
reload(paintlib)
layout,top = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
layout.dbu = 0.001#设置单位长度为1nm
paintlib.IO.pointdistance=2000#设置腔的精度,转弯处相邻两点的距离

import math
#wf2=[6.75 7]
for j in range(6):    
        wf=(5.85+0.05*j )*2*math.pi
        epsilonr=11.4
        epsiloneff=(1+epsilonr)/2
        print("pi: %s" %(math.pi))
        print("sqrt: %s" %(math.sqrt(1.44)))
        cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        print("length1: %s"%(cavitylen))
        #画腔
        painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,290000),angle=90,widout=8000,widin=4000,bgn_ext=0000,end_ext=0000)
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





##
#BP Filter
wp=5.975*2*math.pi
epsilonr=11.4
epsiloneff=(1+epsilonr)/2
cavitylenp1=math.pi*3e8/(2*wp*math.sqrt(epsiloneff))
print("lengthp1: %s"%(cavitylenp1))

painter3=paintlib.CavityPainter(pya.DPoint(-3167000,785000),angle=90,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation
def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=0
    length+=painter.Straight(756000)
    length+=painter.Turning(35000)
    length+=painter.Straight(3050000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(319000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(63070)

    return length


length=painter3.Run(path)
print("length of Filter p1: %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painter3.Draw(cell2,layer1)#把画好的腔置入


###########
for j in range(6):    
        wf=(6.15+0.05*j )*2*math.pi
        epsilonr=11.4
        epsiloneff=(1+epsilonr)/2
        print("pi: %s" %(math.pi))
        print("sqrt: %s" %(math.sqrt(1.44)))
        cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        print("length1: %s"%(cavitylen))
        #画腔
        painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000,290000),angle=90,widout=8000,widin=4000,bgn_ext=0000,end_ext=0000)
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
        
            #entry *(-1)
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





##
#BP Filter
wp=6.275*2*math.pi
epsilonr=11.4
epsiloneff=(1+epsilonr)/2
cavitylenp2=math.pi*3e8/(2*wp*math.sqrt(epsiloneff))
print("lengthp2: %s"%(cavitylenp2))

painter3=paintlib.CavityPainter(pya.DPoint(3167000,785000),angle=90,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation
def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=0
    length+=painter.Straight(756000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(3050000)
    length+=painter.Turning(35000)
    length+=painter.Straight(319000)
    length+=painter.Turning(35000)
    length+=painter.Straight(63070)

    return length


length=painter3.Run(path)
print("length of Filter p1: %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painter3.Draw(cell2,layer1)#把画好的腔置入

##########

for j in range(6):    
        wf=(6.45+0.05*j )*2*math.pi
        epsilonr=11.4
        epsiloneff=(1+epsilonr)/2
        print("pi: %s" %(math.pi))
        print("sqrt: %s" %(math.sqrt(1.44)))
        cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        print("length1: %s"%(cavitylen))
        #画腔
        painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-290000),angle=270,widout=8000,widin=4000,bgn_ext=0000,end_ext=0000)
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

##
#BP Filter
wp=6.575*2*math.pi
epsilonr=11.4
epsiloneff=(1+epsilonr)/2
cavitylenp3=math.pi*3e8/(2*wp*math.sqrt(epsiloneff))
print("lengthp3: %s"%(cavitylenp3))

painter3=paintlib.CavityPainter(pya.DPoint(-3167000,-785000),angle=270,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation
def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=0
    length+=painter.Straight(756000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(3050000)
    length+=painter.Turning(35000)
    length+=painter.Straight(319000)
    length+=painter.Turning(35000)
    length+=painter.Straight(63070)

    return length


length=painter3.Run(path)
print("length of Filter p3: %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painter3.Draw(cell2,layer1)#把画好的腔置入

###########
for j in range(6):    
        wf=(6.75+0.05*j )*2*math.pi
        epsilonr=11.4
        epsiloneff=(1+epsilonr)/2
        print("pi: %s" %(math.pi))
        print("sqrt: %s" %(math.sqrt(1.44)))
        cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        print("length1: %s"%(cavitylen))
        #画腔
        painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-290000),angle=270,widout=8000,widin=4000,bgn_ext=0000,end_ext=0000)
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
        
            #entry *(-1)
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


##
#BP Filter
wp=6.875*2*math.pi
epsilonr=11.4
epsiloneff=(1+epsilonr)/2
cavitylenp4=math.pi*3e8/(2*wp*math.sqrt(epsiloneff))
print("lengthp4: %s"%(cavitylenp4))


Qf4=wp/0.2

Cin=math.sqrt(math.pi/(4*wp*wp*50*50*Qf4*30) )

#zl=1/(i*wp*Cin)+50; phic=phicfun(zl(wp,Cin),50), dc=c*phic/(2*wp*math.sqrt(epsilon_eff))
#Qf4=(math.pi/4)/( math.cos(  (  math.pi*x/(2*cavitylenp4)  )^2 ) )    xx=   ( 2*cavitylenp4* math.sqrt( math.acos( math.pi/4/Qf4 ) ) )/math.pi



painter3=paintlib.CavityPainter(pya.DPoint(3167000,-785000),angle=270,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation
def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=0
    length+=painter.Straight(756000)
    length+=painter.Turning(35000)
    length+=painter.Straight(3050000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(319000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(63070)

    return length


length=painter3.Run(path)
print("length of Filter p4: %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painter3.Draw(cell2,layer1)#把画好的腔置入





#输出
paintlib.IO.Show()#输出到屏幕上
paintlib.IO.Write()#输出到文件中







