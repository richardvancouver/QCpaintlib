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


for j in range(5):
       painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,290000),angle=90,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)

       def path1(painter):
           painter.Straight(100000)
       
           
       painter3.Run(path1)    
       
       try:
          painter3.InterdigitedCapacitor(j)
       except RuntimeError as _:
          painter3.InterdigitedCapacitor(j+1)
#if number%2!=1:raise RuntimeError('number must be odd')  try except RuntimeError as:_
       
       if j%2!=1: raise RuntimeError('number of teeth must be odd')       

       layer1 = layout.layer(10, 0)#创建新层
       cell2 = layout.create_cell("Resonator1")#创建一个子cell
       top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
       painter3.Draw(cell2,layer1)#把画好的腔置入



paintlib.IO.Show()