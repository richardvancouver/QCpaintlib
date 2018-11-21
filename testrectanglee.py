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




class Eraser:
    '''用于画基础图形的静态类'''
    @staticmethod
    def eraserpoly(rectangle3,rectangledielectric):
    
          
          #rectangle3=pya.DPolygon([  pya.DPoint(-50000,55000-40000),pya.DPoint(0,55000-40000),pya.DPoint(0,50000-40000),pya.DPoint(155000,50000-40000), pya.DPoint(155000,150000-40000), pya.DPoint(160000,150000-40000), pya.DPoint(160000,155000-40000),pya.DPoint(0000,155000-40000),pya.DPoint(0000,150000-40000),pya.DPoint(-50000,150000-40000)  ])
          
          
          
          #rectangledielectric=pya.DPolygon([  pya.DPoint(5000,50000),pya.DPoint(100000,50000),pya.DPoint(100000,-50000),pya.DPoint(5000,-50000)])
          
          
          
          
          
          list2=[];
          
          for jj in range(rectangledielectric.num_points_hull()):
              if  rectangle3.inside(rectangledielectric.point_hull(jj)):
                list2.append( rectangledielectric.point_hull(jj) )
          print("list2") #find the points inside the region
          print(list2[0])
          print(list2[1])
          print("------")
          
          
          
          
          listin=[]
          for edg1 in rectangledielectric.each_edge():
              for edg2 in rectangle3.each_edge():
                 if edg1.intersect(edg2):
                     #print(edg1.intersection_point(edg2))
                     listin.append( edg1.intersection_point(edg2) )
          print("listin") #find the intersection points
          print(listin[0])
          print(listin[1])
          
          print("======")  #just put the 'inside' points and the 'intersection' points into rectangle3.insert_hole( [pya.DPoint(10000,10000),pya.DPoint(10000,30000),pya.DPoint(90000,30000),pya.DPoint(90000,10000)] )
          #then, the corresponding overlap part gets erased
          
          listinhole=[]
          for it in listin:
              listinhole.append( pya.DPoint(it.x, it.y) )
          
          for bt in list2:
              listinhole.append( pya.DPoint(bt.x,bt.y) )
          
          #rectangle3.insert_hole( [pya.DPoint(10000,10000),pya.DPoint(10000,30000),pya.DPoint(90000,30000),pya.DPoint(90000,10000)] )
          
          rectangle3.insert_hole( listinhole ) #need topological sorting before inputting listinhole
          return listinhole[0]#rectangle3#listinhole









