try:
    paintlib.IO.layout_view
except NameError as e:
    import paintlib
    layout,top = paintlib.IO.Start("guiopen")
def points(obj):
    if obj.is_box():
        return [obj.box_p1,pya.Point(obj.box_p1.x,obj.box_p2.y),obj.box_p2,pya.Point(obj.box_p2.x,obj.box_p1.y)]
    else:
        return obj.each_point_hull()
print('------------------------------------------------------------------------------------------------------')
fid = open('pymacros/polygons.py','w')
print('import pya',file=fid,end='\n')
strpts='polygons=[' 
for i,data in enumerate(paintlib.IO.layout_view.object_selection):
    ptsxy=[(pt.x,pt.y) for pt in points(data.shape)]
    print('pts%s=[]'%i,file=fid)
    for ptxy in ptsxy:
        print('pts%s.append(pya.DPoint(%s,%s))'%(i,ptxy[0],ptxy[1]),file=fid)
    #help(i)
    strpts+='pya.DPolygon(pts%s),'%i
print('%s]'%strpts,file=fid)
fid.close()
print('print into pymacros/polygons.py')
'''变换
[obj.shape.transform(pya.CplxTrans(1,0,False,1000,0)) for obj in paintlib.IO.layout_view.object_selection];

'''
####
# import pya
# import paintlib
# layout,top = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
# layout.dbu = 0.001#设置单位长度为1nm
# paintlib.IO.pointdistance=500#设置腔的精度,转弯处相邻两点的距离

# from polygons import polygons
# layer = layout.layer(10, 10)
# cell=top
# '[paintlib.BasicPainter.Draw(top,layer,x) for x in polygons]'
# polygonsout=[]
# for x in polygons:
#     if isinstance(x,pya.DPolygon):
#         polygonsout.append(pya.Polygon.from_dpoly(x))
# region1=pya.Region(polygonsout)
# cell.shapes(layer).insert(region1)
# #输出
# paintlib.IO.Show()#输出到屏幕上
####

# print(paintlib.IO.layout_view.each_object_selected())

# layout_view = paintlib.IO.layout_view
# import random
# random.random()
# for j in range(1):
#    for i in layout_view.each_object_selected():    
#        i.shape.transform(pya.CplxTrans((random.random()-0.5)*.2+1,0,False,1000*(random.random()-0.5),1000*(random.random()-0.5)))
#        pass

