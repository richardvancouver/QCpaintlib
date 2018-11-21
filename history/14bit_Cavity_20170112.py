# -*- coding: utf-8 -*-

#初始化
import pya
import history.paintlib20170112 as paintlib
layout,cell = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
layout.dbu = 0.001#设置单位长度为1nm
paintlib.IO.pointdistance=500#设置腔的精度,转弯处相邻两点的距离

#画腔
dy=-250000
painter3=paintlib.CavityPainter(pya.DPoint(0,1050000+dy),angle=-90,widout=48000,widin=16000,bgn_ext=0,end_ext=0)
c1bgninfo=painter3.Getinfo()[0:3]
c1bgninfo[2]+=180
def path1(painter):#设置内轮廓路径
    dl=547.0693762227893-dy/11
    length=0
    length+=painter.Straight(570000+dy)
    length+=painter.Turning(40000)
    length+=painter.Straight(210000+dl)
    length+=painter.Turning(-40000)
    length+=painter.Turning(-40000)
    for i in range(5):
        length+=painter.Straight(500000+dl*2)#1
        length+=painter.Turning(40000)
        length+=painter.Turning(40000)
        length+=painter.Straight(500000+dl*2)#2
        length+=painter.Turning(-40000)
        length+=painter.Turning(-40000)
    length+=painter.Straight(210000+dl)
    length+=painter.Turning(40000)
    length+=painter.Straight(570000+dy)
    print("length of Cavity1 : %s"%(length))
    print("add %s to dl"%((8080000-length)/22))
painter3.Draw(path1)
c1endinfo=painter3.Getinfo()[0:3]
centerlineinfos=[]
regionlistout=[]
regionlistin=[]
centerlineinfos.extend(painter3.centerlineinfos)
regionlistout.extend(painter3.regionlistout)
regionlistin.extend(painter3.regionlistin)

anglelist1=zip([-135, -90, -45, 0, 45, 90, 135],
               [45, 0, 45, 0, -45, 0, -45],range(7))
bgnlen=[125663.70614359167,62831.85307179589,62831.85307179589,
        0,62831.85307179589,62831.85307179589,125663.70614359167]
for angle1,angle2,index in anglelist1:
    painter3.__init__(pya.DPoint(c1bgninfo[0],c1bgninfo[1]),c1bgninfo[2],widout=48000,widin=16000,bgn_ext=0,end_ext=0)
    length=0   
    length+=painter3.Draw(lambda painter:painter.Turning(40000,angle1))
    length+=painter3.Draw(lambda painter:painter.Straight(800000-bgnlen[index]))
    #painter3.end_ext=16000
    length+=painter3.Draw(lambda painter:painter.Turning(40000,angle2))
    print("length of bgn %s : %s"%(index,length))
    print("add %s to bgnlen %s"%(length-800000,index))
    centerlineinfos.extend(painter3.centerlineinfos)
    regionlistout.extend(painter3.regionlistout)
    regionlistin.extend(painter3.regionlistin)
anglelist1=zip([-135, -90, -45, 0, 45, 90, 135],
               [45, 0, 45, 0, -45, 0, -45],range(7))
endlen=[125663.70614359167,62831.85307179589,62831.85307179589,
        0,62831.85307179589,62831.85307179589,125663.70614359167]
for angle1,angle2,index in anglelist1:
    painter3.__init__(pya.DPoint(c1endinfo[0],c1endinfo[1]),c1endinfo[2],widout=48000,widin=16000,bgn_ext=0,end_ext=0)
    length=0   
    length+=painter3.Draw(lambda painter:painter.Turning(40000,angle1))
    length+=painter3.Draw(lambda painter:painter.Straight(800000-endlen[index]))
    #painter3.end_ext=16000
    length+=painter3.Draw(lambda painter:painter.Turning(40000,angle2))
    print("length of bgn %s : %s"%(index,length))
    print("add %s to bgnlen %s"%(length-800000,index))
    centerlineinfos.extend(painter3.centerlineinfos)
    regionlistout.extend(painter3.regionlistout)
    regionlistin.extend(painter3.regionlistin)

painter3.centerlineinfos=centerlineinfos
painter3.regionlistout=regionlistout
painter3.regionlistin=regionlistin

layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Cavity1")#创建一个子cell
cell.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painter3.Output(cell2,layer1)#把画好的腔置入
#    #画Crossover
#centerlinelist=[]#画腔的中心线并根据中心线画Crossover
##centerlinelist.append(painter3.Getcenterlineinfo()[0][0])
#for i in painter3.Getcenterlineinfo():
#    centerlinelist.append(i[0])
#painter4=paintlib.TransfilePainter("[Crossover48].gds","insert")
#painter4.airbrigedistance=100000#设置Crossover的间距
#painter4.DrawAirbrige(cell2,centerlinelist,"Crossover1")


##画边界
#layer2 = layout.layer(1, 1)
#border=paintlib.BasicPainter.DrawBorder(leng=4050000,siz=4050000,wed=50000)
#paintlib.BasicPainter.Output(cell,layer2,border)

#输出
paintlib.IO.Show()#输出到屏幕上
paintlib.IO.Write()#输出到文件中
#