import paintlib180730 as paintlib #paintlib180730 paintlib180804
import pya
from math import cos,sin,pi
Interactive=paintlib.Interactive
CavityPainter=paintlib.CavityPainter
IO=paintlib.IO

class paths:
    @staticmethod
	def path3(painter,cavitylen=0, signn=1):#设置内轮廓路径
		lenthunit=397495.55921538756
		lenthentry=241371.66941154067
		lenthexit=150000
		frac=(cavitylen-lenthexit-lenthentry)/lenthunit
		print("sections: %s"%(frac))
		print("sections: %s"%( math.floor(frac) ))
		remainder=cavitylen-lenthexit-lenthentry-9*lenthunit
		print("remainder: %s"%( remainder ))

		#entry
		length=0
		tinylenth=100000
		length+=painter.Straight(100000)
		length+=painter.Turning(-30000*signn)
		length+=painter.Straight(tinylenth)
		length+=painter.Turning(30000*signn)
		length+=painter.Turning(30000*signn)

		for i in range(9):
			#oldlength=length
			length+=painter.Straight(104500)#1
			length+=painter.Turning(-30000*signn)
			length+=painter.Turning(-30000*signn)
			length+=painter.Straight(104500)#2
			length+=painter.Turning(30000*signn)
			length+=painter.Turning(30000*signn)



		#length+=painter.Straight(150000+remainder)
		length+=painter.Straight(150000)  
		length+=painter.Turning(30000*signn)
		length+=painter.Straight(cavitylen-length)
		return length

