# -*- coding: utf-8 -*-

#初始化
import pya
import paintlib180730b as paintlib
from imp import reload
reload(paintlib)
layout,top = paintlib.IO.Start("guiopen")#在当前的图上继续画,如果没有就创建一个新的
layout.dbu = 0.001#设置单位长度为1nm
paintlib.IO.pointdistance=2000#设置腔的精度,转弯处相邻两点的距离
TBD=paintlib.TBD.init(686587)

JJ=6.175 #MHz
kff=30 #MHz
Dff=5 #MHz
offsetz1=300000


offsetx=[0,500000,500000*2,500000*3,500000*4,500000*5 , 0,500000,500000*2,500000*3,500000*4,500000*5, 0,500000,500000*2,500000*3,500000*4,500000*5, 112000,112000+500000*1,112000+500000*2,112000+500000*3,112000+500000*4,112000+500000*5  , 112000-8000+750,112000-8000+750+500000*1,112000-8000+750+500000*2,112000-8000+750+500000*3,112000-8000+750+500000*4,112000-8000+750+500000*5,  210000,210000+500000*1,210000+500000*2,210000+500000*3,210000+500000*4,210000+500000*5, 210000,210000+500000*1,210000+500000*2,210000+500000*3,210000+500000*4,210000+500000*5,  210000,210000+500000*1,210000+500000*2,210000+500000*3,210000+500000*4,210000+500000*5,   0+190000-2000,0+190000-2000+498000*1,0+190000-2000+498000*2,0+190000-2000+498000*3,0+190000-2000+498000*4,0+190000-2000+498000*5,  0+190000-2000,0+190000-2000+498000*1,0+190000-2000+498000*2,0+190000-2000+498000*3,0+190000-2000+498000*4,0+190000-2000+498000*5,   0,0+500000*1,0+500000*2,0+500000*3,0+500000*4,0+500000*5,     0,0+500000*1,0+500000*2,0+500000*3,0+500000*4,0+500000*5,  0,0+500000*1,0+500000*2,0+500000*3,0+500000*4,0+500000*5,   0+105000,0+105000+500000,0+105000+500000*2,0+105000+500000*3,0+105000+500000*4,0+105000+500000*5,   0+105000+7000,0+105000+500000+7000,0+105000+500000*2+7000,0+105000+500000*3+7000,0+105000+500000*4+7000,0+105000+500000*5+7000, 0+209750,   0+209750,  0+209750   , 0+209750+500000,   0+209750+500000,  0+209750+500000 , 0+209750+500000*2,   0+209750+500000*2,  0+209750+500000*2,   0+209750+500000*3,   0+209750+500000*3,  0+209750+500000*3,   0+209750+500000*4,   0+209750+500000*4,  0+209750+500000*4,   0+209750+500000*5,   0+209750+500000*5,  0+209750+500000*5, 0+185000+3000, 0+185000+3000,   0+185000+3000+498000, 0+185000+3000+498000,   0+185000+3000+498000*2, 0+185000+3000+498000*2,0+185000+3000+498000*3, 0+185000+3000+498000*3,  0+185000+3000+498000*4, 0+185000+3000+498000*4, 0+185000+3000+498000*5, 0+185000+3000+498000*5];
offsety=[0,0,0,0,0,0 , -480000,-480000,-480000,-480000,-480000,-480000, 480000,480000,480000,480000,480000,480000, -480000-125000,-480000-125000,-480000-125000,-480000-125000,-480000-125000,-480000-125000,   -480000-125000+1180000,-480000-125000+1180000,-480000-125000+1180000,-480000-125000+1180000,-480000-125000+1180000,-480000-125000+1180000,    0,0,0,0,0,0,   0+240000,0+240000,0+240000,0+240000,0+240000,0+240000,  0+240000*2,0+240000*2,0+240000*2,0+240000*2,0+240000*2,0+240000*2,  -480000+62000,-480000+62000,-480000+62000,-480000+62000,-480000+62000,-480000+62000,  -480000+62000+240000,-480000+62000+240000,-480000+62000+240000,-480000+62000+240000,-480000+62000+240000,-480000+62000+240000,  1358000,1358000,1358000,1358000,1358000,1358000,  1358000+480000,1358000+480000,1358000+480000,1358000+480000,1358000+480000,1358000+480000, 1358000-480000,1358000-480000,1358000-480000,1358000-480000,1358000-480000,1358000-480000,     1358000-480000-58000,1358000-480000-58000,1358000-480000-58000,1358000-480000-58000,1358000-480000-58000,1358000-480000-58000,    1358000-480000-58000+1140000,1358000-480000-58000+1140000,1358000-480000-58000+1140000,1358000-480000-58000+1140000,1358000-480000-58000+1140000,1358000-480000-58000+1140000,   1358000-480000,    1358000,  1358000-240000,  1358000-480000,    1358000,  1358000-240000, 1358000-480000,    1358000,  1358000-240000, 1358000-480000,    1358000,  1358000-240000, 1358000-480000,    1358000,  1358000-240000, 1358000-480000,    1358000,  1358000-240000,   1358000+420000,   1358000+420000-120000*2,   1358000+420000,   1358000+420000-120000*2, 1358000+420000,   1358000+420000-120000*2, 1358000+420000,   1358000+420000-120000*2, 1358000+420000,   1358000+420000-120000*2, 1358000+420000,   1358000+420000-120000*2];
szz=len(offsetx);









####via and br array######


for ind in range(szz):
    ###########via and br##################
    
    offsetx[ind]
    ####via 1######
    paintervia1,_,_=paintlib.BasicPainter.rectangle(pya.DPoint(-3200000+1380000-959000+8000+offsetx[ind],3100000+offsetz1-120000*2-2200000-36000+2000+offsety[ind]),pya.DPoint(-3200000+1380000-959000+offsetx[ind],3100000+offsetz1-120000*2-2200000-36000+2000+offsety[ind]), 8000) #pointr,pointl,length
    
    #########################################################draw them 
    layer1 = layout.layer(12, 0)#创建新层
    cell2 = layout.create_cell("via")#创建一个子cell
    top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
    paintlib.BasicPainter.Draw(cell2,layer1,paintervia1)#把画好的腔置入
    
    
    ####via 2######
    paintervia1,_,_=paintlib.BasicPainter.rectangle(pya.DPoint(-3200000+1380000-959000+8000+26000+offsetx[ind],3100000+offsetz1-120000*2-2200000-36000+2000+offsety[ind]),pya.DPoint(-3200000+1380000-959000+26000+offsetx[ind],3100000+offsetz1-120000*2-2200000-36000+2000+offsety[ind]), 8000) #pointr,pointl,length
    
    #########################################################draw them 
    layer1 = layout.layer(12, 0)#创建新层
    cell2 = layout.create_cell("via")#创建一个子cell
    top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
    paintlib.BasicPainter.Draw(cell2,layer1,paintervia1)#把画好的腔置入
    
    
    
    ##############br 1#############################################
    painterbr1,_,_=paintlib.BasicPainter.rectangle(pya.DPoint(-3200000+1380000-959000+26000+8000+offsetx[ind],3100000+offsetz1-120000*2-2200000-36000+2000+offsety[ind]),pya.DPoint(-3200000+1380000-959000+offsetx[ind],3100000+offsetz1-120000*2-2200000-36000+2000+offsety[ind]), 8000) #pointr,pointl,length
    
    #########################################################draw them 
    layer1 = layout.layer(13, 0)#创建新层
    cell2 = layout.create_cell("br")#创建一个子cell
    top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
    paintlib.BasicPainter.Draw(cell2,layer1,painterbr1)#把画好的腔置入
    
    
    
    
    ###########via and br##################


















##############start the feedline backbone#############################################
painterfeed1=paintlib.CavityPainter(pya.DPoint(-3200000,3100000+offsetz1-120000*2),angle=0,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)


listbrush=[]
length=0
def pathfeed(painter):
    length=0
    length+=painter.Straight(545700+4300)
    return length


length=painterfeed1.Run(pathfeed)
brushfeed1=painterfeed1.brush ##record T position 1
listbrush.append(brushfeed1)
#print("listbrush is here:")
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

def pathfeedplus(painter):
    length=0
    length+=painter.Straight(50000*3+4.5*1000)
    return length
   
painterfeed1.Run(pathfeedplus)







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
        painter.Straight(50000+7000)
    
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
freqs1pk=[6.095,6.135,6.176,6.216,6.257,6.297 ]
res_fraction_1=[]
flip_fraction_1=[]
for j in range(6):    
       wf=freqs1[j]*2*math.pi #p110 of sank: wf/2pi=6.75GHz
       epsilonr=11.4
       epsiloneff=(1+epsilonr)/2
      # print("pi: %s" %(math.pi))
      # print("sqrt: %s" %(math.sqrt(1.44)))
       cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
       cavitylenflip=math.pi*3e8/(2*(wf-Dff/1000)*math.sqrt(epsiloneff))  #wf*0.995


       qcf=wf*1000/kff #both are in MHz
       cinwf=math.sqrt( math.pi/(qcf*2*wf*1e9*wf*1e9*50*50) )
       ccwf=-2*math.pi*JJ*1e6/(wf*1e9*(wf*1e9-Dff*1e6)*50)

       #print("cavitylength sec1_ %s: %s"  %(j, cavitylen))
       #print("flipcavitylength sec1_ %s: %s"  %(j, cavitylenflip))

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
      
      
      
           for i in range(8):
              # #oldlength=length
               length+=painter.Straight(100000+25000+3500-j*2000)#1
               length+=painter.Turning(-30000)
               length+=painter.Turning(-30000)
               length+=painter.Straight(100000+25000+3500-j*2000)#2
               length+=painter.Turning(30000)
               length+=painter.Turning(30000)
      
      
      
          # #length+=painter.Straight(150000+remainder)
           length+=painter.Straight(150000-75000)  
           #length+=painter.Turning(30000)
           #length+=painter.Straight(cavitylen-length)
           return length
      
      
       length=painter3.Run(path3)
       brushbottom=painter3.brush

       
       def path3p(painter): #, length=0
           dlength1=0
           dlength1+=painter.Straight(75000)
           dlength1+=painter.Turning(30000)
           #length+=painter.Turning(-30000)
           dlength1+=painter.Straight(cavitylen-length-dlength1) #100000  +length
           return dlength1
          #return painter.Straight(5000)
       dlength1b=painter3.Run(path3p)
       #dlength1=painter3.Run(path3p)
       #length=length+dlength1
       #print("cc-tail length sec1_ %s: %s"  %(j, dlength1b))
       #print("cc-tail_length/cavity_length sec1_ %s: %s" %(j, dlength1b/cavitylen)   )
       res_fraction_1.append( dlength1b/cavitylen )
       painterup=paintlib.CavityPainter(brushbottom)
       

       def patht(painter):    #for turning 180degree, to position the brush
          painter.Straight(50000)
          painter.Turning(50000,270)
          painter.Straight(50000)
      
       painterup.Run(patht)
       brushupb=painterup.brush


       def pathup(painter):
           return painter.Straight(34000+63.799*1000)

       painterc2=paintlib.CavityPainter(brushupb)
       painterc2.Run(pathup)
       painterc2.InterdigitedCapacitor(2*4+1, arg1=3000+27.3*1000*2/3,arg2=45000,arg3=31000,arg4=4000,arg5=3000,arg6=3000,arg7=2000)#cc#.InterdigitedCapacitor(2*1+1, arg1=3000+27.3*1000*2/3,arg2=45000,arg3=31000,arg4=4000,arg5=3000,arg6=3000,arg7=2000)

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
       
       painter3=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000+67500,290000+1308000+offsetz1-120000),angle=180,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)
       painter3plus=paintlib.CavityPainter(pya.DPoint(-2650000+j*500000+67500,290000+1308000+offsetz1-120000),angle=0,widout=8000,widin=4000,bgn_ext=000,end_ext=0000)

#       def pathtail(painter):
#           lengthtail=0
#           lengthtail+=painter.Straight(0000)
#           lengthtail+=painter.Turning(-30000)
#           lengthtail+=painter.Straight(100000)
#       lengthtail1=painter3plus.Run(pathtail) 
       length=0





       def patha(painter):
          length=0
          length+=painter.Straight(75000-0.25*1000)
          return length
   
       length1=painter3.Run(patha) # need to return a value to length1, otherwise length1 is non-type
       brushf1=painter3.brush


       def path3(painter):#设置内轮廓路径
          # #painter.Turning(40000)
          # #painter.Straight(50000)
          # #painter.Turning(40000)
      
      
           length=0#length1
           #print("j is here")
           #print(j)
           tinylenth=100000     
      
           length+=painter.Straight(150000-75000) 

           for i in range(8):
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
       painter3.InterdigitedCapacitor(2*4+1)

####the tail########
       def pathtail(painter):
           lengthtail=0
           lengthtail+=painter.Straight(0000)
           lengthtail+=painter.Turning(-30000)
           lengthtail+=painter.Straight(cavitylenflip-length1-length-lengthtail)
           return lengthtail
       lengthtail1=painter3plus.Run(pathtail)
       #print("flip's cc-tail_length sec1_ %s: %s" %(j,length1+lengthtail1))
       #print("flip's cc-tail_length/flip_cavity_length sec1_ %s: %s" %(j,(length1+lengthtail1)/cavitylenflip ))
       flip_fraction_1.append( (length1+lengthtail1)/cavitylenflip )
#####################################################################       
       painterdn=paintlib.CavityPainter(brushf1)
       

       def patht(painter):    #for turning 180degree, to position the brush
          painter.Straight(50000)
          painter.Turning(50000,270)
          painter.Straight(50000)
      
       painterdn.Run(patht)
       brushdnb=painterdn.brush


       def pathdn(painter):
           return painter.Straight(40000+89000)

       painterc2=paintlib.CavityPainter(brushdnb)
       painterc2.Run(pathdn)
#######################################################################       
       
############merge before drawing####################       
       painter3.regionlistout.extend(painterc2.regionlistout) #list action, extend the list of painter3
       painter3.regionlistin.extend(painterc2.regionlistin)
       painter3.regionlistout.extend(painter3plus.regionlistout)  
       painter3.regionlistin.extend(painter3plus.regionlistin)
############merge before drawing####################       

      # #print("length of resonator1 : %s"%(length))
       layer1 = layout.layer(10, 0)#创建新层
       cell2 = layout.create_cell("Resonator1")#创建一个子cell
       top.insert(pya.CellInstArray(cell2.cell_index(),pya.Trans()))
       painter3.Draw(cell2,layer1)#把画好的腔置入
       ##########      


#####################################
      

#####################################

       painter3p5=paintlib.CavityPainter(pya.DPoint(-2840000+j*500000,1576000+1824000),angle=0,widout=8000,widin=4000,bgn_ext=000,end_ext=000)#indicating the transmission line position

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

       painter1=paintlib.TransfilePainter("C:/Users/Rui/Desktop/g/sqc-painter/Qubit-24bitv2cd.gds") #Qubit-24bitv2c   Qubit-24bitv2c Qubit-24bitv2c2

       pts=[pya.Point(-2750000+j*500000,140000)]
       xx=pts[0].x+11000
       yy=pts[0].y+850000-200000 #one side's distance to the center is longer than the other side, and the generated box is symmetric to the center, thus add some offsets to capture both sides, otherwise one side will be cutted and the other side will be missed
       portbrushs=[
            paintlib.CavityBrush(pointc=pya.DPoint(xx+2739000 -2657.25*1000,yy-790000+1704000),angle=0,widout=8000,widin=4000,bgn_ext=0),
            paintlib.CavityBrush(pointc=pya.DPoint(xx+2739000 -2750000 ,yy-790000+4000+24000 ),angle=0,widout=8000,widin=4000,bgn_ext=0),
            #paintlib.CavityBrush(pointc=pya.DPoint(xx+0,yy-136000),angle=0,widout=8000,widin=4000,bgn_ext=0)

       ]
       
       painter1.DrawMark(top,pts,"qubit"+str(j))
#
       import simulationtrilayerb
       reload(simulationtrilayerb)
       Simulation=simulationtrilayerb.Simulation
        
       layerlist=[(10,0)]
       layerlistvia1=[(12,0)]
       layerlistbr1=[(13,0)]
        # box=pya.Box(-848740,-212112,40934,424224)
        # paintlib.Interactive.cut(layerlist=layerlist,layermod='in',box=box) 5 to 7GHz
        #boxx=530000-22000,boxy=1607000+100000
       Simulation.create(
           name='tttriof'+str(j),startfrequency=freqs1pk[j]-0.015,endfrequency=freqs1pk[j]+0.015,stepfrequency=2/300,
           layerlist=layerlist,layerlistvia=layerlistvia1,layerlistbr=layerlistbr1,boxx=530000-22000,boxy=1750000*2-300000 -1500000 -24000,
           region=None,brush=None,transmissionlines=None,portbrushs=portbrushs,
           offsetx=0,offsety=0,deltaangle=0,absx=xx-22000/2,absy=yy+60000+900000-300000/2 -1500000/2+4000 +24000/2
           )
        
        
        #输出
#       print(TBD.isFinish())
       paintlib.IO.Show()#输出到屏幕上
        #paintlib.IO.Write()#输出到文件中
        #


#####################################################################################
#####################################################################################


























































