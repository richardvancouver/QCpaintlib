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
        wf=(5.85+0.05*j )*2*math.pi #p110 of sank: wf/2pi=6.75GHz
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

#Qf=wp/bandwidth
Qf1=wp/(2*math.pi)/0.2
print("Qf1: %s"%Qf1)
#interdigited capacitor module
Cin1=math.sqrt(math.pi/(4*wp*1e9*wp*1e9*50*50*Qf1*30) )

#dc=0
zl1=1/(1j*wp*1e9*Cin1)+50
print("zl1.real: %s"%zl1.real)
print("zl1.imag: %s"%zl1.imag)

argu1=(zl1-50)/(zl1+50)
print("argu1.real: %s"%argu1.real)
print("argu1.imag: %s"%argu1.imag)

phic1=math.atan(argu1.imag/argu1.real)

print("phic1: %s" %phic1)
dc1=3e8*phic1/(2*wp*math.sqrt(epsiloneff)) #electrical length of the interdigited capacitor
print("dc1: %s"%dc1)
print("Qf1: %s"%Qf1)
print("tapx1/lenp1: %s" %(math.sqrt(math.asin(math.pi/4/Qf1))  /(math.pi/2) ))

tapx1= ( 2*cavitylenp1* math.sqrt( math.asin( math.pi/4/Qf1 ) ) )/math.pi
print("tap1: %s"%tapx1)
print(math.pi*tapx1/(2*cavitylenp1))

painter3=paintlib.CavityPainter(pya.DPoint(-3167000,785000),angle=90,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation

def pathb(painter):
    return painter.Straight(tapx1)


def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=tapx1
    length+=painter.Straight(756000-length)
    length+=painter.Turning(35000)
    length+=painter.Straight(3050000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(cavitylenp1-dc1-length)
    #length+=painter.Turning(-35000)
    #length+=painter.Straight(63070)

    return length


painter3.Run(pathb)
brush=painter3.brush
length=painter3.Run(path)
painter3.InterdigitedCapacitor(3) #add the capacitor

print("length of Filter p1: %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))

def patht(painter):
    painter.Straight(50000)
    painter.Turning(50000,270)
    painter.Straight(50000)
paintert=paintlib.CavityPainter(brush)
paintert.Run(patht)
brush=paintert.brush

def pathc2(painter):
    painter.Straight(100000)
painterc2=paintlib.CavityPainter(brush)
painterc2.Run(pathc2)

painter3.regionlistout.extend(painterc2.regionlistout)
painter3.regionlistin.extend(painterc2.regionlistin)
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


#Qf=wp/bandwidth
Qf2=wp/(2*math.pi)/0.2

#interdigited capacitor module
Cin2=math.sqrt(math.pi/(4*wp*1e9*wp*1e9*50*50*Qf2*30) )

#dc=0
zl2=1/(1j*wp*1e9*Cin2)+50
print("zl2.real: %s"%zl2.real)
print("zl2.imag: %s"%zl2.imag)

argu2=(zl2-50)/(zl2+50)
print("argu2.real: %s"%argu2.real)
print("argu2.imag: %s"%argu2.imag)

phic2=math.atan(argu2.imag/argu2.real)

print("phic2: %s" %phic2)
dc2=3e8*phic2/(2*wp*math.sqrt(epsiloneff)) #electrical length of the interdigited capacitor
print("dc2: %s"%dc2)

print("Qf2: %s"%Qf2)
print("tapx2/lenp2: %s" %(math.sqrt(math.asin(math.pi/4/Qf2))  /(math.pi/2) ))

tapx2= ( 2*cavitylenp2* math.sqrt( math.asin( math.pi/4/Qf2 ) ) )/math.pi
print("tap2: %s"%tapx2)

painter3=paintlib.CavityPainter(pya.DPoint(3167000,785000),angle=90,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation

#
def pathb(painter):
    return painter.Straight(tapx2)
#


def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=tapx2
    length+=painter.Straight(756000-length)
    length+=painter.Turning(-35000)
    length+=painter.Straight(3050000)
    length+=painter.Turning(35000)
    length+=painter.Straight(cavitylenp2-dc2-length)
    #length+=painter.Turning(-35000)
    #length+=painter.Straight(63070)

    return length

#
painter3.Run(pathb)
brush=painter3.brush
#
length=painter3.Run(path) #painter5.InterdigitedCapacitor(3)
painter3.InterdigitedCapacitor(3) #add the capacitor

print("length of Filter p2: %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))

#
def patht(painter):
    painter.Straight(50000)
    painter.Turning(-50000,270)
    painter.Straight(50000)
paintert=paintlib.CavityPainter(brush)
paintert.Run(patht)
brush=paintert.brush

def pathc2(painter):
    painter.Straight(100000)
painterc2=paintlib.CavityPainter(brush)
painterc2.Run(pathc2)

painter3.regionlistout.extend(painterc2.regionlistout)
painter3.regionlistin.extend(painterc2.regionlistin)
#

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


#Qf=wp/bandwidth
Qf3=wp/(2*math.pi)/0.2

#interdigited capacitor module
Cin3=math.sqrt(math.pi/(4*wp*1e9*wp*1e9*50*50*Qf3*30) )

#dc=0
zl3=1/(1j*wp*1e9*Cin3)+50
print("zl3.real: %s"%zl3.real)
print("zl3.imag: %s"%zl3.imag)

argu3=(zl3-50)/(zl3+50)
print("argu3.real: %s"%argu3.real)
print("argu3.imag: %s"%argu3.imag)

phic3=math.atan(argu3.imag/argu3.real)

print("phic3: %s" %phic3)
dc3=3e8*phic3/(2*wp*math.sqrt(epsiloneff)) #electrical length of the interdigited capacitor
print("dc3: %s"%dc3)

print("Qf3: %s"%Qf3)
print("tapx3/lenp3: %s" %(math.sqrt(math.asin(math.pi/4/Qf3))  /(math.pi/2)) )

tapx3= ( 2*cavitylenp3* math.sqrt( math.asin( math.pi/4/Qf3 ) ) )/math.pi
print("tap3: %s"%tapx3)

painter3=paintlib.CavityPainter(pya.DPoint(-3167000,-785000),angle=270,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation

#
def pathb(painter):
    return painter.Straight(tapx3)
#

def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=tapx3
    length+=painter.Straight(756000-length)
    length+=painter.Turning(-35000)
    length+=painter.Straight(3050000)
    length+=painter.Turning(35000)
    length+=painter.Straight(cavitylenp3-dc3-length)
    #length+=painter.Turning(-35000)
    #length+=painter.Straight(63070)

    return length

#
painter3.Run(pathb)
brush=painter3.brush
#
length=painter3.Run(path)
painter3.InterdigitedCapacitor(3) #add the capacitor

print("length of Filter p3: %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))

#
def patht(painter):
    painter.Straight(50000)
    painter.Turning(-50000,270)
    painter.Straight(50000)
paintert=paintlib.CavityPainter(brush)
paintert.Run(patht)
brush=paintert.brush

def pathc2(painter):
    painter.Straight(100000)
painterc2=paintlib.CavityPainter(brush)
painterc2.Run(pathc2)

painter3.regionlistout.extend(painterc2.regionlistout)
painter3.regionlistin.extend(painterc2.regionlistin)
#

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



#Qf=wp/bandwidth
Qf4=wp/(2*math.pi)/0.2

#interdigited capacitor module
Cin4=math.sqrt(math.pi/(4*wp*1e9*wp*1e9*50*50*Qf4*30) )

#dc=0
zl4=1/(1j*wp*1e9*Cin4)+50
print("zl4.real: %s"%zl4.real)
print("zl4.imag: %s"%zl4.imag)

argu4=(zl4-50)/(zl4+50)
print("argu4.real: %s"%argu4.real)
print("argu4.imag: %s"%argu4.imag)

phic4=math.atan(argu4.imag/argu4.real)

print("phic4: %s" %phic4)
dc4=3e8*phic4/(2*wp*math.sqrt(epsiloneff)) #electrical length of the interdigited capacitor
print("dc4: %s"%dc4)


print("Qf4: %s"%Qf4)
print("tapx4/lenp4: %s" %(math.sqrt(math.asin(math.pi/4/Qf4))  /(math.pi/2)))

tapx4= ( 2*cavitylenp4* math.sqrt( math.asin( math.pi/4/Qf4 ) ) )/math.pi
print("tap4: %s"%tapx4)
print(math.pi*tapx4/(2*cavitylenp4))
#zl=1/(1j*wp*Cin)+50; phic=phicfun(zl(wp,Cin),50), dc=c*phic/(2*wp*math.sqrt(epsilon_eff))
#Qf4=(math.pi/4)/( math.cos(  (  math.pi*x/(2*cavitylenp4)  )^2 ) )    xx=   ( 2*cavitylenp4* math.sqrt( math.acos( math.pi/4/Qf4 ) ) )/math.pi



painter3=paintlib.CavityPainter(pya.DPoint(3167000,-785000),angle=270,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation

#
def pathb(painter):
    return painter.Straight(tapx4)
#

def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=tapx4
    length+=painter.Straight(756000-length)
    length+=painter.Turning(35000)
    length+=painter.Straight(3050000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(cavitylenp4-dc4-length) #reserve some length for Cin
    #length+=painter.Turning(-35000)
    #length+=painter.Straight(63070)

    return length

#
painter3.Run(pathb)
brush=painter3.brush
#

length=painter3.Run(path)
painter3.InterdigitedCapacitor(3) #add the capacitor

print("length of Filter p4: %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))

#
def patht(painter):
    painter.Straight(50000)
    painter.Turning(50000,270) #turn to positive(right-hand-sided) side, rotating 270degree
    painter.Straight(50000)
paintert=paintlib.CavityPainter(brush)
paintert.Run(patht)
brush=paintert.brush

def pathc2(painter):
    painter.Straight(100000)
painterc2=paintlib.CavityPainter(brush)
painterc2.Run(pathc2)

painter3.regionlistout.extend(painterc2.regionlistout)
painter3.regionlistin.extend(painterc2.regionlistin)
#

painter3.Draw(cell2,layer1)#把画好的腔置入





#输出
paintlib.IO.Show()#输出到屏幕上
paintlib.IO.Write()#输出到文件中











