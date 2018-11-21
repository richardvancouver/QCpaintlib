
# Enter your Python code here
from imp import reload
import testclassb
reload(testclassb)


tr=testclassb.testclass

tt=tr.gettap(1,1e-3,1,1)
print("tt:%s"%tt)