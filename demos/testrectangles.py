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





#画腔
painter3=paintlib.CavityPainter(pya.DPoint(0,24000),angle=180,widout=48000,widin=16000,bgn_ext=48000,end_ext=16000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation
def path(painter):#设置内轮廓路径
    painter.Turning(40000)
    painter.Straight(50000)
    painter.Turning(40000)
    for i in range(7):
        painter.Straight(500000-10000)#1
        painter.Turning(-40000)
        painter.Turning(-40000)
        painter.Straight(500000-10000)#2
        painter.Turning(40000)
        painter.Turning(40000)
    painter.Straight(28500)
painter3.Run(path)

layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Cavity1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painter3.Draw(cell2,layer1)#把画好的腔置入

a,b,c=paintlib.BasicPainter.rectangle(pya.DPoint(0,-50000), pya.DPoint(0,50000),100000)
paintlib.BasicPainter.Draw(cell2,layer1,a)



rectangle1=pya.DPolygon([pya.DPoint(0,50000),pya.DPoint(0,150000),pya.DPoint(160000,150000),pya.DPoint(160000,140000),pya.DPoint(155000,140000),pya.DPoint(155000,50000)    ])
rectangle2=pya.DPolygon([pya.DPoint(0,-50000),pya.DPoint(0,-150000),pya.DPoint(160000,-150000),pya.DPoint(160000,-140000),pya.DPoint(155000,-140000),pya.DPoint(155000,-50000)    ])

paintlib.BasicPainter.Draw(cell2,layer1,rectangle1)
paintlib.BasicPainter.Draw(cell2,layer1,rectangle2)




    #画Crossover
centerlinelist=[]#画腔的中心线并根据中心线画Crossover
centerlinelist.append(painter3.Getcenterlineinfo()[0][0])
painter4=paintlib.TransfilePainter("[Crossover48].gds")
painter4.airbridgedistance=100000#设置Crossover的间距
painter4.DrawAirbridge(top,centerlinelist,"Crossover1")

#画电极传输线
cell3 = layout.create_cell("TR1")#创建一个子cell
top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))

painter5=paintlib.CavityPainter(pya.DPoint(-600000,24000),angle=180,widout=20000,widin=10000,bgn_ext=0,end_ext=0)
painter5.Electrode(reverse=True)
def path(painter):
    length=0
    length+=painter.Straight(100000)
    length+=painter.Turning(50000)
    length+=painter.Straight(20000)
    return length
painter5.Run(path)
painter5.InterdigitedCapacitor(9)
dy=TBD.get()
dx=TBD.get()
def path(painter):
    length=0
    length+=painter.Straight(200000+dy)
    length+=painter.Turning(50000)
    length+=painter.Straight(dx)
    return length
painter5.Run(path)
painter5.Narrow(8000,4000,6000)
painter5.end_ext=2000
painter5.Run(lambda painter:painter.Straight(50000))
TBD.set(-500000-painter5.brush.centerx)
TBD.set(600000-painter5.brush.centery,-2)
painter5.Draw(cell3,layer1)

#画边界
layer2 = layout.layer(1, 1)
border=paintlib.BasicPainter.Border(leng=3050000,siz=3050000,wed=50000)
paintlib.BasicPainter.Draw(top,layer2,border)

#画文字
painter2=paintlib.PcellPainter()
painter2.DrawText(top,layer2,"Python",pya.DCplxTrans(100,15,False,1000000,0))

#画Mark
painter1=paintlib.TransfilePainter("[Mark3inch_jiguangzhixie].gds")
pts=[pya.Point(1000000,500000),pya.Point(-500000,-500000),pya.Point(1000000,-1000000)]
painter1.DrawMark(top,pts,"Mark_laserwrite")

#
painter6=paintlib.TransfilePainter("[Xmon_20170112].gds")
tr=pya.DCplxTrans(1,-90,False,400000,-400000)
painter6.DrawGds(top,"Qubit",tr)




#画腔
painter3=paintlib.CavityPainter(pya.DPoint(150000,24000),angle=90,widout=30000,widin=20000,bgn_ext=0000,end_ext=0000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation
def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    painter.Straight(40000)
    painter.Turning(-20000,270)
    painter.Straight(80000)
    painter.Turning(-20000,270)
    painter.Straight(80000)
    
    
painter3.Run(path)


painter3b=paintlib.CavityPainter(pya.DPoint(150000,64000),angle=0,widout=26000,widin=16000,bgn_ext=0000,end_ext=0000)

#def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
#    painter.Straight(80000)
#    painter.Turning(80000,270)
    
#painter3b.Run(path)
    
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Cavity1b")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painter3.Draw(cell2,layer1)#把画好的腔置入
#painter3b.Draw(cell2,layer1)#把画好的腔置入






ddh=8


##draw the PI-shaped part:
painter3=paintlib.CavityPainter(pya.DPoint(-2500000,785000),angle=90,widout=20000,widin=10000,bgn_ext=0000,end_ext=00000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation

def pathb(painter):
    return painter.Straight(40000+80000+20000*ddh)  #####vert len




def pathbb(painter):
    return painter.Straight(5000)

painter3.Run(pathb)
brush=painter3.brush


#length=painter3.Run(path)
painter3.Run(pathbb)
#painter3.InterdigitedCapacitor(3) #add the capacitor

#print("length of Filter p1: %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))

def patht(painter):
    painter.Straight(30000)
    painter.Turning(30000,270)
    painter.Straight(30000)
paintert=paintlib.CavityPainter(brush)
paintert.Run(patht)
brush=paintert.brush #keep the current brush


def pathc2(painter):
    painter.Straight(100000) #define path   ###horizontal width
painterc2=paintlib.CavityPainter(brush) #pick up the current brush
painterc2.Run(pathc2) #run


brush=painterc2.brush #keep the current brush

#brush1=painterc2.brush


painter3.regionlistout.extend(painterc2.regionlistout)
painter3.regionlistin.extend(painterc2.regionlistin)
#painter3.Draw(cell2,layer1)#把画好的腔置入




def patht(painter):
    painter.Straight(30000)
    painter.Turning(30000,270)
    painter.Straight(30000)  #define path
paintertb=paintlib.CavityPainter(brush) #pick up the current brush
paintertb.Run(patht) #run
brush=paintertb.brush
def pathc2b(painter):
    painter.Straight(40000+80000+20000*ddh)  ######vert len
painterc3=paintlib.CavityPainter(brush)
painterc3.Run(pathc2b)




painter3.regionlistout.extend(painterc3.regionlistout)
painter3.regionlistin.extend(painterc3.regionlistin)
#painter3.Draw(cell2,layer1)#把画好的腔置入



###top###

###add another piece####
painter3d=paintlib.CavityPainter(pya.DPoint(-2600000,835000-2500+80000 +20000*ddh),angle=180,widout=5000,widin=10000,bgn_ext=5000,end_ext=00000)

def pathc2bb(painter):
    painter.Straight(0000)
painter3d.Run(pathc2bb)


painter3.regionlistout.extend(painter3d.regionlistout)
painter3.regionlistin.extend(painter3d.regionlistin)
######


###add another piece####
painter3db=paintlib.CavityPainter(pya.DPoint(-2600000-5000,835000-2500-2500+80000 +20000*ddh),angle=180,widout=10000,widin=10000,bgn_ext=5000,end_ext=00000)

def pathc2bbb(painter):
    painter.Straight(0000)
painter3db.Run(pathc2bbb)


painter3.regionlistout.extend(painter3db.regionlistout)
painter3.regionlistin.extend(painter3db.regionlistin)
######

#painter3.regionlistout.extend(painterc3.regionlistout)
#painter3.regionlistin.extend(painterc3.regionlistin)
#################

###add another piece####
painter3dbb=paintlib.CavityPainter(pya.DPoint(-2495000-0000,835000-2500-2500+80000 +20000*ddh),angle=0,widout=10000,widin=10000,bgn_ext=5000,end_ext=00000)

def pathc2bbbb(painter):
    painter.Straight(0000)
painter3dbb.Run(pathc2bbbb)


painter3.regionlistout.extend(painter3dbb.regionlistout)
painter3.regionlistin.extend(painter3dbb.regionlistin)
######


###add another piece####
painter3dbb2=paintlib.CavityPainter(pya.DPoint(-2495000-0000,835000-2500-2500+80000 +20000*ddh),angle=180,widout=10000,widin=10000,bgn_ext=5000,end_ext=00000)

def pathc2bbbb2(painter):
    painter.Straight(0000)
painter3dbb2.Run(pathc2bbbb2)


painter3.regionlistout.extend(painter3dbb2.regionlistout)
painter3.regionlistin.extend(painter3dbb2.regionlistin)
######


##bottom
###add another piece####

painter3dbb3=paintlib.CavityPainter(pya.DPoint(-2500000-0000,780000-80000+80000-0000),angle=90,widout=20000,widin=10000,bgn_ext=5000,end_ext=00000)

def pathc2bbbb3(painter):
    painter.Straight(0000)
painter3dbb3.Run(pathc2bbbb3)


painter3.regionlistout.extend(painter3dbb3.regionlistout)
painter3.regionlistin.extend(painter3dbb3.regionlistin)
######


###add another piece####
painter3dbb4=paintlib.CavityPainter(pya.DPoint(-2600000-0000,780000-80000+80000-0000),angle=90,widout=20000,widin=10000,bgn_ext=5000,end_ext=00000)

def pathc2bbbb4(painter):
    painter.Straight(0000)
painter3dbb4.Run(pathc2bbbb4)


painter3.regionlistout.extend(painter3dbb4.regionlistout)
painter3.regionlistin.extend(painter3dbb4.regionlistin)


#######

painter3.Draw(cell2,layer1)#把画好的腔置入


#输出
print(TBD.isFinish())
paintlib.IO.Show()#输出到屏幕上
paintlib.IO.Write()#输出到文件中
#

