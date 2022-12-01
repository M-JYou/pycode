# coding:utf-8

from typing import Dict


new_tuple=tuple
tuple1=tuple((1,2,3,4,5,6))
tuple2=(1,2)
tuple3=('helloworld')
tuple4=(1)
tuple5=(1,)
tuple6=tuple1+tuple5
a=dict()
b={"name":"mjy","sex":"man"}
if __name__=="__main__":
  print(new_tuple)
  print(tuple1)
  print(type(new_tuple))
  print(tuple2)
  print(tuple3)
  print(type(tuple3))
  print(tuple4)
  print(type(tuple4))
  print(tuple5)
  print(type(tuple5))
  print(tuple6)
  print(id(tuple6))
  print(0 not in (1,2,3,4))
  print (10 not in (1,2,3,4))
  print(len(tuple5))
  print((0>=1,))
  print(a)
  print(b)
  print(1!=2)
  print(3<=4)