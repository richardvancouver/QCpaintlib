# -*- coding: utf-8 -*-

#初始化
import pya
import paintlib180730c as paintlib #paintlib180730c is basically the same as paintlib180730b, just changed draw airbridge part
from imp import reload
reload(paintlib)
layout,top = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
layout.dbu = 0.001#设置单位长度为1nm
paintlib.IO.pointdistance=2000#设置腔的精度,转弯处相邻两点的距离
TBD=paintlib.TBD.init(6876587)





painter1=paintlib.CavityPainter(pya.DPoint(0,2400000-335000-80000-50000),angle=270,widout=8000,widin=4000,bgn_ext=0,end_ext=0)
painter1.Electrode(wid=450000,length=440000+50000,midwid=250000,midlength=250000,narrowlength=120000,reverse=True)#wid=368000,length=360000,midwid=200000,midlength=200000,narrowlength=120000,reverse=False#
def path(painter):
    length=0
    length+=painter.Straight(100000-21000)
    length+=painter.Turning(50000)
    length+=painter.Straight(20000+1952000-24000+2000)





#    length+=painter.Turning(129000)
#    length+=painter.Straight(1871000)






    length+=painter.Turning(-129000)
    length+=painter.Turning(-129000)
#    length+=painter.Straight(4000000)
#    length+=painter.Turning(129000)
#    length+=painter.Turning(129000)
#    length+=painter.Straight(4000000)
#    length+=painter.Turning(-129000)
#    length+=painter.Turning(-129000)
    for kk in range(13):
        length+=painter.Straight(4000000)
        length+=painter.Turning(129000*math.pow((-1),(kk)))
        length+=painter.Turning(129000*math.pow((-1),(kk)))   
    
    
    length+=painter.Straight(2000000-129000)
    length+=painter.Turning(-129000)
    #length+=painter.Straight(50000)

#    length+=painter.Turning(-129000)
     
    return length
painter1.Run(path)
painter1.Electrode(wid=450000,length=440000+50000,midwid=250000,midlength=250000,narrowlength=120000,reverse=False)#wid=368000,length=360000,midwid=200000,midlength=200000,narrowlength=120000,reverse=False#

layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Cavity1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans(pya.Trans.R0)))
painter1.Draw(cell2,layer1)#把画好的腔置入
    #画Crossover
centerlinelist=[]#画腔的中心线并根据中心线画Crossover
centerlinelist.append(painter1.Getcenterlineinfo()[0][0])

print(centerlinelist[0][0]) #(painter1.Getcenterlineinfo()[0][0])#(centerlinelist[0][0])
centerlinelistb=[ centerlinelist[0][100:] ] #leave blank at the beginning centerlinelist[0][i+50] for i in range(10)

painter4=paintlib.TransfilePainter("[JJunite].gds") #JJunit [JJAb]#modify crossover, one type is for defining JJ areas, another type is for normal crossover
painter4.airbridgedistance=75000*2+16000#100000#设置Crossover的间距
painter4.DrawAirbridge(top,centerlinelistb,"CrossoverJJ")




#输出
#print(TBD.isFinish())
paintlib.IO.Show()#输出到屏幕上
#paintlib.IO.Write()#输出到文件中
#

