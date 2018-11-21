
# Enter your Python code here
from math import cos,sin,pi,sqrt,asin,atan
class testclass:

      #def__init__(self):
         #self.water=0
         
         
      @staticmethod
      def gettap(w,bandwidth,epsilonef,lenth):
          Qf=w/(2*pi)/bandwidth
          #interdigited capacitor module
          Cin=sqrt(pi/(4*w*1e9*w*1e9*50*50*Qf*30) )
          
          #dc=0
          zl=1/(1j*w*1e9*Cin)+50#+para3
      
          argu=(zl-50)/(zl+50)
          phic=atan(argu.imag/argu.real)
          #dc=3e8*phic/(2*w*math.sqrt(epsilonef)) #electrical length of the interdigited capacitor
          print("Qf in gettap:%s" %Qf)
          tapx= ( 2*lenth*sqrt( asin( pi/4/Qf ) ) )/pi
      
      
          return tapx#dc