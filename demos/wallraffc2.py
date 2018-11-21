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


##############start the feedline backbone#############################################
painterfeed1=paintlib.CavityPainter(pya.DPoint(-3200000,3100000),angle=0,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)


listbrush=[]
length=0
def pathfeed(painter):
    length=0
    length+=painter.Straight(545700)
    return length


length=painterfeed1.Run(pathfeed)
brushfeed1=painterfeed1.brush ##record T position 1
listbrush.append(brushfeed1)
print("listbrush is here:")
print(listbrush[0])
#######################################################################################


#######keep going right##############


def pathfeed(painter):
    length=0
    length+=painter.Straight(500000)
    return length

for k in range(5):    
    length=painterfeed1.Run(pathfeed)
    listbrush.append(painterfeed1.brush) ##record T position 2
###################################









for kk in range(6):
    ####make brush point down and go to the position###
    painterfeeddn1=paintlib.CavityPainter(listbrush[kk])
    def pathturn1(painter):
        painter.Straight(50000)
        painter.Turning(50000,-270)
        painter.Straight(50000)
        
    painterfeeddn1.Run(pathturn1)
    brushfeeddn1b=painterfeeddn1.brush    
    ################################################
    
    #####make the downward CPW segment###############
    painterfeeddn1b=paintlib.CavityPainter(brushfeeddn1b)
    
    def pathfeeddn1(painter):
        painter.Straight(50000)
    
    painterfeeddn1b.Run(pathfeeddn1)
    #####################################
    ####################################################combine the segments
    painterfeed1.regionlistout.extend(painterfeeddn1b.regionlistout) #list action, extend the list of painter3
    painterfeed1.regionlistin.extend(painterfeeddn1b.regionlistin)
    
    ####################################################
















#########################################################draw them 
layer1 = layout.layer(10, 0)#创建新层
cell2 = layout.create_cell("feed1")#创建一个子cell
top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
painterfeed1.Draw(cell2,layer1)#把画好的腔置入
#########################################################

#########resonator sec1############
freqs1=[6.4463,6.4941,6.5424,6.5915,6.6413,6.6914 ]
for j in range(6):    
       wf=(5.85+0.05*j +0.3)*2*math.pi #p110 of sank: wf/2pi=6.75GHz
       epsilonr=11.4
       epsiloneff=(1+epsilonr)/2
      # print("pi: %s" %(math.pi))
      # print("sqrt: %s" %(math.sqrt(1.44)))
       cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
      # print("length1: %s"%(cavitylen))
      # #画腔
       painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,290000),angle=90,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
      # #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
      # #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
      
      
      
      
      
       def path3(painter):#设置内轮廓路径
          # #painter.Turning(40000)
          # #painter.Straight(50000)
          # #painter.Turning(40000)
      
      
      
      
      
      
           lenthunit=397495.55921538756
           lenthentry=241371.66941154067
           lenthexit=150000
           frac=(cavitylen-lenthexit-lenthentry)/lenthunit
          # print("sections: %s"%(frac))
          # print("sections: %s"%( math.floor(frac) ))
           remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
          # print("remainder: %s"%( remainder ))
      
          # #entry
           length=0
           tinylenth=100000
           length+=painter.Straight(100000)
           length+=painter.Turning(-30000)
           length+=painter.Straight(tinylenth-50000+2250)
           length+=painter.Turning(30000)
           length+=painter.Turning(30000)
      
      
      
           for i in range(9):
              # #oldlength=length
               length+=painter.Straight(100000+25000+3500-j*2000)#1
               length+=painter.Turning(-30000)
               length+=painter.Turning(-30000)
               length+=painter.Straight(100000+25000+3500-j*2000)#2
               length+=painter.Turning(30000)
               length+=painter.Turning(30000)
      
      
      
          # #length+=painter.Straight(150000+remainder)
           length+=painter.Straight(150000)  
           #length+=painter.Turning(30000)
           #length+=painter.Straight(cavitylen-length)
           return length
      
      
       length=painter3.Run(path3)
       brushbottom=painter3.brush


       def path3p(painter):
          return painter.Straight(5000)

       painter3.Run(path3p)
       length=length+5000


       painterup=paintlib.CavityPainter(brushbottom)
       

       def patht(painter):    #for turning 180degree, to position the brush
          painter.Straight(50000)
          painter.Turning(50000,270)
          painter.Straight(50000)
      
       painterup.Run(patht)
       brushupb=painterup.brush


       def pathup(painter):
           return painter.Straight(34000)

       painterc2=paintlib.CavityPainter(brushupb)
       painterc2.Run(pathup)

       painter3.regionlistout.extend(painterc2.regionlistout) #list action, extend the list of painter3
       painter3.regionlistin.extend(painterc2.regionlistin)
       #painter3.Draw(cell2,layer1)#把画好的腔置入
      #painter3.InterdigitedCapacitor(3)
      # #print("length of resonator1 : %s"%(length))
       layer1 = layout.layer(10, 0)#创建新层
       cell2 = layout.create_cell("Resonator1")#创建一个子cell
       top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
       painter3.Draw(cell2,layer1)#把画好的腔置入
       
       
       ######flipped resonator1#####
       
       painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000+67500,290000+1308000),angle=180,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
       length=0





       def patha(painter):
          length=0
          length+=painter.Straight(5000)
          return length
   
       length1=painter3.Run(patha) # need to return a value to length1, otherwise length1 is non-type
       brushf1=painter3.brush


       def path3(painter):#设置内轮廓路径
          # #painter.Turning(40000)
          # #painter.Straight(50000)
          # #painter.Turning(40000)
      
      
           length=length1
           print("j is here")
           print(j)
           tinylenth=100000     
      
           length+=painter.Straight(150000) 

           for i in range(9):
              # #oldlength=length


               
               length+=painter.Turning(30000)
               length+=painter.Turning(30000)
               length+=painter.Straight(100000+25000+3500-j*2000)#2
               length+=painter.Turning(-30000)
               length+=painter.Turning(-30000)
               length+=painter.Straight(100000+25000+3500-j*2000)#1


           lenthunit=397495.55921538756
           lenthentry=241371.66941154067
           lenthexit=150000
           frac=(cavitylen-lenthexit-lenthentry)/lenthunit
          # print("sections: %s"%(frac))
          # print("sections: %s"%( math.floor(frac) ))
           remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
          # print("remainder: %s"%( remainder ))
      
          # #entry




           length+=painter.Turning(30000)
           length+=painter.Turning(30000)
           length+=painter.Straight(tinylenth-50000+2250)      
           length+=painter.Turning(-30000)      
           length+=painter.Straight(100000)

      

      
      
      
          # #length+=painter.Straight(150000+remainder)
           #length+=painter.Straight(150000)  
           #length+=painter.Turning(30000)
           #length+=painter.Straight(cavitylen-length)
           return length
      
       
       length=painter3.Run(path3)
       painter3.InterdigitedCapacitor(3)

#####################################################################       
       painterdn=paintlib.CavityPainter(brushf1)
       

       def patht(painter):    #for turning 180degree, to position the brush
          painter.Straight(50000)
          painter.Turning(50000,270)
          painter.Straight(50000)
      
       painterdn.Run(patht)
       brushdnb=painterdn.brush


       def pathdn(painter):
           return painter.Straight(40000)

       painterc2=paintlib.CavityPainter(brushdnb)
       painterc2.Run(pathdn)
#######################################################################       
       
############merge before drawing####################       
       painter3.regionlistout.extend(painterc2.regionlistout) #list action, extend the list of painter3
       painter3.regionlistin.extend(painterc2.regionlistin)
############merge before drawing####################       

      # #print("length of resonator1 : %s"%(length))
       layer1 = layout.layer(10, 0)#创建新层
       cell2 = layout.create_cell("Resonator1")#创建一个子cell
       top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
       painter3.Draw(cell2,layer1)#把画好的腔置入
       ##########      


#####################################
      

#####################################

       painter3p5=paintlib.CavityPainter(pya.DPoint(-2840000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        #brush=painter3.brush

       painter4=paintlib.CavityPainter(pya.DPoint(-2840000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        # def path(painter):
            # painter.Straight(200000)
            
        # painter4.Run(path)
        # layer1 = layout.layer(10, 0)#创建新层
        # cell3 = layout.create_cell("Trans1")#创建一个子cell
        # top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        # painter4.Draw(cell3,layer1)
        # c4=painter4.Getcenterlineinfo()
        # print("C4:%s" %c4)

#################qubits sec1############

       painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2c2.gds")

       pts=[pya.Point(-2750000+j*500000,140000)]
       xx=pts[0].x+11000
       yy=pts[0].y+850000-200000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        #portbrushs=[
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    #]
       painter1.DrawMark(top,pts,"qubit"+str(j))
#
       import simulation
       reload(simulation)
       Simulation=simulation.Simulation
        
       layerlist=[(10,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box) 5 to 7GHz
        
       Simulation.create(
           name='Wallraffb'+str(j),startfrequency=freqs1[j]-0.001,endfrequency=freqs1[j]+0.001,stepfrequency=2/300,
           layerlist=layerlist,boxx=530000-22000,boxy=1607000+100000,
           region=None,brush=painter3p5.brush,transmissionlines=None,portbrushs=None,
           offsetx=0,offsety=0,deltaangle=0,absx=xx-22000/2,absy=yy+60000
           )
        
        
        #输出
       print(TBD.isFinish())
       paintlib.IO.Show()#输出到屏幕上
        #paintlib.IO.Write()#输出到文件中
        #






###################section 2#################
freqs2=[6.7429,6.795,6.848,6.9019,6.9565,7.0119]
for j in range(6):    
         wf=(6.15+0.05*j +0.3)*2*math.pi #p110 of sank: wf/2pi=6.75GHz
         epsilonr=11.4
         epsiloneff=(1+epsilonr)/2
        # print("pi: %s" %(math.pi))
        # print("sqrt: %s" %(math.sqrt(1.44)))
         cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        # print("length1: %s"%(cavitylen))
        # #画腔
         painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000,290000),angle=90,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
        # #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        # #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
         def path3(painter):#设置内轮廓路径
            # #painter.Turning(40000)
            # #painter.Straight(50000)
            # #painter.Turning(40000)
        
        
        
        
        
        
             lenthunit=397495.55921538756
             lenthentry=241371.66941154067
             lenthexit=150000
             frac=(cavitylen-lenthexit-lenthentry)/lenthunit
            # print("sections: %s"%(frac))
            # print("sections: %s"%( math.floor(frac) ))
             remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
            # print("remainder: %s"%( remainder ))
        
            # #entry
             length=0
             tinylenth=100000
             length+=painter.Straight(100000)
             length+=painter.Turning(-30000*(-1))
             length+=painter.Straight(tinylenth-50000+2250)
             length+=painter.Turning(30000*(-1))
             length+=painter.Turning(30000*(-1))
        
        
        
             for i in range(9):
                # #oldlength=length
                 length+=painter.Straight(104500+25000+3500-16500-j*2000)#1
                 length+=painter.Turning(-30000*(-1))
                 length+=painter.Turning(-30000*(-1))
                 length+=painter.Straight(104500+25000+3500-16500-j*2000)#2
                 length+=painter.Turning(30000*(-1))
                 length+=painter.Turning(30000*(-1))
        
        
        
            # #length+=painter.Straight(150000+remainder)
             length+=painter.Straight(150000)  
             #length+=painter.Turning(30000*(-1))
             #length+=painter.Straight(cavitylen-length)
             return length
        
        
         length=painter3.Run(path3)
        
        # #print("length of resonator1 : %s"%(length))
         layer1 = layout.layer(10, 0)#创建新层
         cell2 = layout.create_cell("Resonator1")#创建一个子cell
         top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
         painter3.Draw(cell2,layer1)#把画好的腔置入

       ######flipped resonator2#####
       
         painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000-67500,290000+1308000),angle=0,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
  
         def path3(painter):#设置内轮廓路径
            # #painter.Turning(40000)
            # #painter.Straight(50000)
            # #painter.Turning(40000)
        
        
             length=0
             tinylenth=100000     
        
             length+=painter.Straight(150000) 
  
             for i in range(9):
                # #oldlength=length
  
  
                 
                 length+=painter.Turning(-30000)
                 length+=painter.Turning(-30000)
                 length+=painter.Straight(100000+25000+3500-16500-j*2000)#2
                 length+=painter.Turning(30000)
                 length+=painter.Turning(30000)
                 length+=painter.Straight(100000+25000+3500-16500-j*2000)#1
  
  
             lenthunit=397495.55921538756
             lenthentry=241371.66941154067
             lenthexit=150000
             frac=(cavitylen-lenthexit-lenthentry)/lenthunit
            # print("sections: %s"%(frac))
            # print("sections: %s"%( math.floor(frac) ))
             remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
            # print("remainder: %s"%( remainder ))
        
            # #entry
  
  
  
  
             length+=painter.Turning(-30000)
             length+=painter.Turning(-30000)
             length+=painter.Straight(tinylenth-50000+2250)      
             length+=painter.Turning(30000)      
             length+=painter.Straight(100000)
  
        
  
        
        
        
            # #length+=painter.Straight(150000+remainder)
             #length+=painter.Straight(150000)  
             #length+=painter.Turning(30000)
             #length+=painter.Straight(cavitylen-length)
             return length
        
        
         length=painter3.Run(path3)
         painter3.InterdigitedCapacitor(3)
        # #print("length of resonator1 : %s"%(length))
         layer1 = layout.layer(10, 0)#创建新层
         cell2 = layout.create_cell("Resonator1")#创建一个子cell
         top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
         painter3.Draw(cell2,layer1)#把画好的腔置入
       ##########      




         painter3p5=paintlib.CavityPainter(pya.DPoint(150000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        #brush=painter3.brush

         painter4=paintlib.CavityPainter(pya.DPoint(150000+j*500000,1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        # def path(painter):
            # painter.Straight(200000)
            
        # painter4.Run(path)
        # layer1 = layout.layer(10, 0)#创建新层
        # cell3 = layout.create_cell("Trans1")#创建一个子cell
        # top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        # painter4.Draw(cell3,layer1)
        # c4=painter4.Getcenterlineinfo()
        # print("C4:%s" %c4)

#################qubits sec2############

        # painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cmirror2.gds")

         pts=[pya.Point(250000+j*500000,140000)]
         xx=pts[0].x+11000
         yy=pts[0].y+850000-200000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        #portbrushs=[
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    #]
        # painter1.DrawMark(top,pts,"qubit"+str(6+j))
#
         import simulation
         reload(simulation)
         Simulation=simulation.Simulation
        
         layerlist=[(10,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
         Simulation.create(
            name='Wallraffb'+str(6+j),startfrequency=freqs2[j]-0.001,endfrequency=freqs2[j]+0.001,stepfrequency=2/300,
            layerlist=layerlist,boxx=530000-22000,boxy=1607000+100000,
            region=None,brush=painter3p5.brush,transmissionlines=None,portbrushs=None,
            offsetx=0,offsety=0,deltaangle=0,absx=xx-22000/2,absy=yy+60000
            )
        
        
        #输出
         print(TBD.isFinish())
         paintlib.IO.Show()#输出到屏幕上
        #paintlib.IO.Write()#输出到文件中
        #



###################section 3#################
freqs3=[6.4249,6.4723,6.5205,6.5693,6.6234,6.6738]
for j in range(6):    
         wf=(6.45+0.05*j +0.3)*2*math.pi #p110 of sank: wf/2pi=6.75GHz
         epsilonr=11.4
         epsiloneff=(1+epsilonr)/2
        # print("pi: %s" %(math.pi))
        # print("sqrt: %s" %(math.sqrt(1.44)))
         cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        # print("length1: %s"%(cavitylen))
        # #画腔
         painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-290000),angle=270,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
        # #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        # #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
         def path3(painter):#设置内轮廓路径
            # #painter.Turning(40000)
            # #painter.Straight(50000)
            # #painter.Turning(40000)
        
        
        
        
        
        
             lenthunit=397495.55921538756
             lenthentry=241371.66941154067
             lenthexit=150000
             frac=(cavitylen-lenthexit-lenthentry)/lenthunit
            # print("sections: %s"%(frac))
            # print("sections: %s"%( math.floor(frac) ))
             remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
            # print("remainder: %s"%( remainder ))
        
            # #entry
             length=0
             tinylenth=100000
             length+=painter.Straight(100000)
             length+=painter.Turning(-30000*(-1))
             length+=painter.Straight(tinylenth-50000+2250)
             length+=painter.Turning(30000*(-1))
             length+=painter.Turning(30000*(-1))
        
        
        
             for i in range(9):
                # #oldlength=length
                 length+=painter.Straight(100000+25000+3500+4000-j*2000)#1
                 length+=painter.Turning(-30000*(-1))
                 length+=painter.Turning(-30000*(-1))
                 length+=painter.Straight(100000+25000+3500+4000-j*2000)#2
                 length+=painter.Turning(30000*(-1))
                 length+=painter.Turning(30000*(-1))
        
        
        
            # #length+=painter.Straight(150000+remainder)
             length+=painter.Straight(150000)  
             #length+=painter.Turning(30000*(-1))
             #length+=painter.Straight(cavitylen-length)
             return length
        
        
         length=painter3.Run(path3)
        
        # #print("length of resonator1 : %s"%(length))
         layer1 = layout.layer(10, 0)#创建新层
         cell2 = layout.create_cell("Resonator1")#创建一个子cell
         top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
         painter3.Draw(cell2,layer1)#把画好的腔置入


       ######flipped resonator3#####
       
         painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000+67500,-290000-1308000),angle=180,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)

         def path3(painter):#设置内轮廓路径
            # #painter.Turning(40000)
            # #painter.Straight(50000)
            # #painter.Turning(40000)
        
        
             length=0
             tinylenth=100000     
        
             length+=painter.Straight(150000) 
  
             for i in range(9):
                # #oldlength=length
  
  
                 
                 length+=painter.Turning(-30000)
                 length+=painter.Turning(-30000)
                 length+=painter.Straight(100000+25000+3500+4000-j*2000)#2
                 length+=painter.Turning(30000)
                 length+=painter.Turning(30000)
                 length+=painter.Straight(100000+25000+3500+4000-j*2000)#1
  
  
             lenthunit=397495.55921538756
             lenthentry=241371.66941154067
             lenthexit=150000
             frac=(cavitylen-lenthexit-lenthentry)/lenthunit
            # print("sections: %s"%(frac))
            # print("sections: %s"%( math.floor(frac) ))
             remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
            # print("remainder: %s"%( remainder ))
        
            # #entry
  
  
  
  
             length+=painter.Turning(-30000)
             length+=painter.Turning(-30000)
             length+=painter.Straight(tinylenth-50000+2250)      
             length+=painter.Turning(30000)      
             length+=painter.Straight(100000)
  
        
  
        
        
        
            # #length+=painter.Straight(150000+remainder)
             #length+=painter.Straight(150000)  
             #length+=painter.Turning(30000)
             #length+=painter.Straight(cavitylen-length)
             return length
        
        
         length=painter3.Run(path3)
         painter3.InterdigitedCapacitor(3)        
        # #print("length of resonator1 : %s"%(length))
         layer1 = layout.layer(10, 0)#创建新层
         cell2 = layout.create_cell("Resonator1")#创建一个子cell
         top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
         painter3.Draw(cell2,layer1)#把画好的腔置入
       ##########      

         painter3p5=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position
  
          #brush=painter3.brush
  
         painter4=paintlib.CavityPainter(pya.DPoint(-2840000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)
  
          # def path(painter):
              # painter.Straight(200000)
              
          # painter4.Run(path)
          # layer1 = layout.layer(10, 0)#创建新层
          # cell3 = layout.create_cell("Trans1")#创建一个子cell
          # top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
          # painter4.Draw(cell3,layer1)
          # c4=painter4.Getcenterlineinfo()
          # print("C4:%s" %c4)
  
  #################qubits sec3############
  
          # painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cm32.gds")
  
         pts=[pya.Point(-2750000+j*500000,-140000-14000)]
         xx=pts[0].x+11000
         yy=pts[0].y-850000+200000-45.5*1000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
          #portbrushs=[
          #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
          #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
          #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)
  
      #]
          # painter1.DrawMark(top,pts,"qubit"+str(12+j))
  #
         import simulation
         reload(simulation)
         Simulation=simulation.Simulation
        
         layerlist=[(10,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
         Simulation.create(
            name='Wallraffb'+str(12+j),startfrequency=freqs3[j]-0.001,endfrequency=freqs3[j]+0.001,stepfrequency=2/300,
            layerlist=layerlist,boxx=530000-22000,boxy=1607000+100000,
            region=None,brush=painter3p5.brush,transmissionlines=None,portbrushs=None,
            offsetx=0,offsety=0,deltaangle=0,absx=xx-22000/2,absy=yy
            )
        
        
        #输出
         print(TBD.isFinish())
         paintlib.IO.Show()#输出到屏幕上
        #paintlib.IO.Write()#输出到文件中
        #





###################section 4#################
freqs4=[6.7249,6.7769,6.825,6.8786,6.933,6.9886]
for j in range(6):    
         wf=(6.75+0.05*j +0.3)*2*math.pi #p110 of sank: wf/2pi=6.75GHz
         epsilonr=11.4
         epsiloneff=(1+epsilonr)/2
        # print("pi: %s" %(math.pi))
        # print("sqrt: %s" %(math.sqrt(1.44)))
         cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
        # print("length1: %s"%(cavitylen))
        # #画腔
         painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-290000),angle=270,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
        # #painter3.painterin.Turning=painter3.painterin.TurningInterpolation
        # #painter3.painterout.Turning=painter3.painterout.TurningInterpolation
        
        
        
        
        
         def path3(painter):#设置内轮廓路径
            # #painter.Turning(40000)
            # #painter.Straight(50000)
            # #painter.Turning(40000)
        
        
        
        
        
        
             lenthunit=397495.55921538756
             lenthentry=241371.66941154067
             lenthexit=150000
             frac=(cavitylen-lenthexit-lenthentry)/lenthunit
            # print("sections: %s"%(frac))
            # print("sections: %s"%( math.floor(frac) ))
             remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
            # print("remainder: %s"%( remainder ))
        
            # #entry
             length=0
             tinylenth=100000
             length+=painter.Straight(100000)
             length+=painter.Turning(-30000*(1))
             length+=painter.Straight(tinylenth-50000+2250)
             length+=painter.Turning(30000*(1))
             length+=painter.Turning(30000*(1))
        
        
        
             for i in range(9):
                # #oldlength=length
                 length+=painter.Straight(104500+25000+3500+4000-16500-j*2000)#1
                 length+=painter.Turning(-30000*(1))
                 length+=painter.Turning(-30000*(1))
                 length+=painter.Straight(104500+25000+3500+4000-16500-j*2000)#2
                 length+=painter.Turning(30000*(1))
                 length+=painter.Turning(30000*(1))
        
        
        
            # #length+=painter.Straight(150000+remainder)
             length+=painter.Straight(150000)  
             #length+=painter.Turning(30000*(1))
             #length+=painter.Straight(cavitylen-length)
             return length
        
        
         length=painter3.Run(path3)
        
        # #print("length of resonator1 : %s"%(length))
         layer1 = layout.layer(10, 0)#创建新层
         cell2 = layout.create_cell("Resonator1")#创建一个子cell
         top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
         painter3.Draw(cell2,layer1)#把画好的腔置入

       ######flipped resonator4#####
       
         painter3=paintlib.CavityPainter(pya.DPoint(150000+j*500000-67500,-290000-1308000),angle=0,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
  
         def path3(painter):#设置内轮廓路径
            # #painter.Turning(40000)
            # #painter.Straight(50000)
            # #painter.Turning(40000)
        
        
             length=0
             tinylenth=100000     
        
             length+=painter.Straight(150000) 
  
             for i in range(9):
                # #oldlength=length
  
  
                 
                 length+=painter.Turning(30000)
                 length+=painter.Turning(30000)
                 length+=painter.Straight(100000+25000+3500+4000-16500-j*2000)#2
                 length+=painter.Turning(-30000)
                 length+=painter.Turning(-30000)
                 length+=painter.Straight(100000+25000+3500+4000-16500-j*2000)#1
  
  
             lenthunit=397495.55921538756
             lenthentry=241371.66941154067
             lenthexit=150000
             frac=(cavitylen-lenthexit-lenthentry)/lenthunit
            # print("sections: %s"%(frac))
            # print("sections: %s"%( math.floor(frac) ))
             remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
            # print("remainder: %s"%( remainder ))
        
            # #entry
  
  
  
  
             length+=painter.Turning(30000)
             length+=painter.Turning(30000)
             length+=painter.Straight(tinylenth-50000+2250)      
             length+=painter.Turning(-30000)      
             length+=painter.Straight(100000)
  
        
  
        
        
        
            # #length+=painter.Straight(150000+remainder)
             #length+=painter.Straight(150000)  
             #length+=painter.Turning(30000)
             #length+=painter.Straight(cavitylen-length)
             return length
        
        
         length=painter3.Run(path3)
         painter3.InterdigitedCapacitor(3)        
        # #print("length of resonator1 : %s"%(length))
         layer1 = layout.layer(10, 0)#创建新层
         cell2 = layout.create_cell("Resonator1")#创建一个子cell
         top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
         painter3.Draw(cell2,layer1)#把画好的腔置入
       ##########      


         painter3p5=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)#indicating the transmission line position

        #brush=painter3.brush

         painter4=paintlib.CavityPainter(pya.DPoint(150000+j*500000,-1576000),angle=0,widout=20000,widin=10000,bgn_ext=000,end_ext=000)

        # def path(painter):
            # painter.Straight(200000)
            
        # painter4.Run(path)
        # layer1 = layout.layer(10, 0)#创建新层
        # cell3 = layout.create_cell("Trans1")#创建一个子cell
        # top.insert(pya.CellInstArray(cell3.cell_index(),pya.Trans()))
        # painter4.Draw(cell3,layer1)
        # c4=painter4.Getcenterlineinfo()
        # print("C4:%s" %c4)

#################qubits sec4############

        # painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cmirrorb2.gds")

         pts=[pya.Point(250000+j*500000,-140000-14000)]
         xx=pts[0].x+11000
         yy=pts[0].y-850000+200000-45.5*1000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
        #portbrushs=[
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx-116000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+100000,yy+150000-7000),angle=0,widout=8000,widin=4000,bgn_ext=0),
        #    paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

    #]
        # painter1.DrawMark(top,pts,"qubit"+str(18+j))
#
         import simulation
         reload(simulation)
         Simulation=simulation.Simulation
        
         layerlist=[(10,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box)
        
         Simulation.create(
            name='Wallraffb'+str(18+j),startfrequency=freqs4[j]-0.001,endfrequency=freqs4[j]+0.001,stepfrequency=2/300,
            layerlist=layerlist,boxx=530000-22000,boxy=1607000+100000,
            region=None,brush=painter3p5.brush,transmissionlines=None,portbrushs=None,
            offsetx=0,offsety=0,deltaangle=0,absx=xx-22000/2,absy=yy
            )
        
        
        #输出
         print(TBD.isFinish())
         paintlib.IO.Show()#输出到屏幕上
        #paintlib.IO.Write()#输出到文件中
        #












