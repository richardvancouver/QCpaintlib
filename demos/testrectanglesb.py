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







layer1 = layout.layer(10, 10)#创建新层
cell2 = layout.create_cell("Cavity1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))

a,b,c=paintlib.BasicPainter.rectangle(pya.DPoint(0,-50000), pya.DPoint(0,50000),100000)
#paintlib.BasicPainter.Draw(cell2,layer1,a)



rectangle1=pya.DPolygon([  pya.DPoint(0,50000),pya.DPoint(0,150000),pya.DPoint(160000,150000),pya.DPoint(160000,140000),pya.DPoint(155000,140000),pya.DPoint(155000,50000)    ])
rectangle2=pya.DPolygon([  pya.DPoint(0,-50000),pya.DPoint(0,-150000),pya.DPoint(160000,-150000),pya.DPoint(160000,-140000),pya.DPoint(155000,-140000),pya.DPoint(155000,-50000)    ])

#paintlib.BasicPainter.Draw(cell2,layer1,rectangle1)
#paintlib.BasicPainter.Draw(cell2,layer1,rectangle2)


rectangle3=pya.DPolygon([  pya.DPoint(-50000,55000-40000),pya.DPoint(0,55000-40000),pya.DPoint(0,50000-40000),pya.DPoint(155000,50000-40000), pya.DPoint(155000,150000-40000), pya.DPoint(160000,150000-40000), pya.DPoint(160000,155000-40000),pya.DPoint(0000,155000-40000),pya.DPoint(0000,150000-40000),pya.DPoint(-50000,150000-40000)  ])
#rectangle4=pya.DPolygon([  pya.DPoint(-50000,-55000),pya.DPoint(0,-55000),pya.DPoint(0,-50000),pya.DPoint(0,-150000),pya.DPoint(160000,-150000),pya.DPoint(160000,-140000),pya.DPoint(155000,-140000),pya.DPoint(155000,-50000)    ])
rectangle4=pya.DPolygon([  pya.DPoint(-50000,-55000+40000),pya.DPoint(0,-55000+40000),pya.DPoint(0,-50000+40000),pya.DPoint(155000,-50000+40000), pya.DPoint(155000,-150000+40000), pya.DPoint(160000,-150000+40000), pya.DPoint(160000,-155000+40000),pya.DPoint(0000,-155000+40000),pya.DPoint(0000,-150000+40000),pya.DPoint(-50000,-150000+40000)  ])

#paintlib.BasicPainter.Draw(cell2,layer1,rectangle3)
paintlib.BasicPainter.Draw(cell2,layer1,rectangle4)

rectangledielectric=pya.DPolygon([  pya.DPoint(5000,50000),pya.DPoint(100000,50000),pya.DPoint(100000,-50000),pya.DPoint(5000,-50000)])
paintlib.BasicPainter.Draw(cell2,layer1,rectangledielectric)


#print("rec31:%s",%rectangle3[1])
#rectangle3[1]
 
 
#layer1.inside_part(rectangle4)
list1=[1,1]
#print(list1)
tt=rectangle3.num_points_hull()
#print(tt)
#tt
for jj in range(rectangle3.num_points_hull()):
    if not rectangledielectric.inside(rectangle3.point_hull(jj)):
        list1.append( rectangledielectric.point_hull(jj) )
        
if not rectangledielectric.inside(pya.DPoint(0,0)):
        list1.append(pya.DPoint(0,0))

        
#print(rectangledielectric.point_hull(jj))        
print(list1)
print("------")


list2=[];

for jj in range(rectangledielectric.num_points_hull()):
    if  rectangle3.inside(rectangledielectric.point_hull(jj)):
        list2.append( rectangledielectric.point_hull(jj) )
print("list2")
print(list2[0])
print(list2[1])
print("------")
edge=pya.DEdge(0,0,10,10)
edge2=pya.DEdge(0,0,10,20)
edge.intersection_point(edge2).x
edge.intersection_point(edge2).y

for edg in rectangledielectric.each_edge():
    print(edg)



for edg1 in rectangledielectric.each_edge():
    for edg2 in rectangle3.each_edge():
         if edg1.intersect(edg2):
             print(edg1.intersection_point(edg2))


print("======")  #just put the 'inside' points and the 'intersection' points into rectangle3.insert_hole( [pya.DPoint(10000,10000),pya.DPoint(10000,30000),pya.DPoint(90000,30000),pya.DPoint(90000,10000)] )
#then, the corresponding overlap part gets erased

print(rectangle3.num_points_hull())
print(rectangle3.num_points_hole(0))
for jj in range(rectangle3.num_points_hull()):
        print( rectangle3.point_hull(jj).x )
        print( rectangle3.point_hull(jj).y )


rectangle3.insert_hole( [pya.DPoint(10000,10000),pya.DPoint(10000,30000),pya.DPoint(90000,30000),pya.DPoint(90000,10000)] )
print("======")
print("======")
print(rectangle3.num_points_hull())
print(rectangle3.num_points_hole(0))
for jj in range(rectangle3.num_points_hull()):
        print( rectangle3.point_hull(jj).x )
        print( rectangle3.point_hull(jj).y )
        
print("hole pnts")        
for jj in range(rectangle3.num_points_hole(0)):
        print( rectangle3.point_hull(jj).x )
        print( rectangle3.point_hull(jj).y )


paintlib.BasicPainter.Draw(cell2,layer1,rectangle3)
##    if rectangle4.inside(rectangle3.point_hull(jj))
#    list1.extend( rectangle3.point_hull(jj) )
#输出
#print(TBD.isFinish())
paintlib.IO.Show()#输出到屏幕上
paintlib.IO.Write()#输出到文件中
#



