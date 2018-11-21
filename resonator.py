
# Enter your Python code here

import pya
import paintlib
from imp import reload
reload(paintlib)
layout,top = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
layout.dbu = 0.001#设置单位长度为1nm
paintlib.IO.pointdistance=2000#设置腔的精度,转弯处相邻两点的距离

#画腔
painter3=paintlib.CavityPainter(pya.DPoint(0,24000),angle=90,widout=8000,widin=4000,bgn_ext=8000,end_ext=4000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation
def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=0
    length+=painter.Straight(100000)
    length+=painter.Turning(-30000)
    length+=painter.Straight(52250)
    length+=painter.Turning(30000)
    length+=painter.Turning(30000)
    for i in range(9):
        length+=painter.Straight(104500)#1
        length+=painter.Turning(-30000)
        length+=painter.Turning(-30000)
        length+=painter.Straight(104500)#2
        length+=painter.Turning(30000)
        length+=painter.Turning(30000)
    length+=painter.Straight(150000)
    return length


length=painter3.Run(path)
print("length of resonator1 : %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Resonator1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painter3.Draw(cell2,layer1)#把画好的腔置入

centerlinelist=[]#画腔的中心线并根据中心线画Crossover
centerlinelist.append(painter3.Getcenterlineinfo()[0][0])
painter4=paintlib.TransfilePainter("[Crossover48].gds","insert")
painter4.airbridgedistance=50000#设置Crossover的间距
painter4.DrawAirbridge(top,centerlinelist,"Crossover1")


#画电极传输线
cell3 = layout.create_cell("icapacitor")#创建一个子cell
top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
#polygon1=paintlib.BasicPainter.Electrode(-500000,24000,angle=0,widout=20000,widin=10000,wid=368000,length=360000,midwid=200000,midlength=200000,narrowlength=120000)
#paintlib.BasicPainter.Draw(cell3,layer1,polygon1)






#painter5=paintlib.CavityPainter(pya.DPoint(-500000,24000),angle=90,widout=20000,widin=10000,bgn_ext=0,end_ext=0)
#painter5.Run(lambda painter:painter.Straight(319000))
#painter5.Run(lambda painter:painter.Turning(35000))
#painter5.Run(lambda painter:painter.Straight(67270))
painter5.InterdigitedCapacitor(3)
#painter5.Run(lambda painter:painter.Straight(92400))
#painter5.Run(lambda painter:painter.Turning(-35000))
#painter5.Run(lambda painter:painter.Straight(431000))






#painter5.Narrow(8000,4000,6000)
#painter5.end_ext=2000
#painter5.Run(lambda painter:painter.Straight(50000))
painter5.Draw(cell3,layer1)




#Filter
#画腔
painter3=paintlib.CavityPainter(pya.DPoint(0,24000),angle=90,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
#painter3.painterin.Turning=painter3.painterin.TurningInterpolation
#painter3.painterout.Turning=painter3.painterout.TurningInterpolation
def path(painter):#设置内轮廓路径
    #painter.Turning(40000)
    #painter.Straight(50000)
    #painter.Turning(40000)

    length=0
    length+=painter.Straight(536000)
    length+=painter.Turning(35000)
    length+=painter.Straight(3050000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(319000)
    length+=painter.Turning(-35000)
    length+=painter.Straight(63070)

    return length


length=painter3.Run(path)
print("length of Filter : %s"%(length))
layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Filter1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painter3.Draw(cell2,layer1)#把画好的腔置入




#输出
paintlib.IO.Show()#输出到屏幕上
paintlib.IO.Write()#输出到文件中