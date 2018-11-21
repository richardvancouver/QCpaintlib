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
    painter1.DrawMark(top,pts,"qubit"+str(j))
#end


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
    painter2.DrawMark(top,pts,"qubit"+str(6+j))
#end




#####sec3
painter3=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cm3.gds")
for j in range(6):
    pts=[pya.Point(-2750000+j*500000,-140000-14000)]
    painter3.DrawMark(top,pts,"qubit"+str(12+j))









#######sec4#
#painter4=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cm4.gds")
painter4=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cmirrorb.gds")

for j in range(6):
    pts=[pya.Point(250000+j*500000,-140000-14000)]
    painter4.DrawMark(top,pts,"qubit"+str(18+j))
#end






#输出
#print(TBD.isFinish())
paintlib.IO.Show()#输出到屏幕上
#paintlib.IO.Write()#输出到文件中
#

