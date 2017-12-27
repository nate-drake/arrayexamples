import secrets
from array import *
myarray=array('i',[1,2,3,4,5,6,7,8,9,10])
roll = secrets.choice(range(0,len(myarray)))
print (myarray[roll])
