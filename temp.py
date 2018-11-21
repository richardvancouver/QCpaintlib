class CavityBrush(object):
    def __init__(self,*args):
        if isinstance(args[0],tuple) and (type(args[1]) in [int,float]):
            self.constructors1(*args)
    def constructors1(self,pointc=(0,8000),angle=0,widout=20000,widin=10000,bgn_ext=0,end_ext=0):
        self.pointc=pointc
        self.widout=widout
        self.end_ext=end_ext
a=CavityBrush((1,2),1,2)
a
