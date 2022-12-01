# coding:utf-8

from cgi import print_arguments
from hashlib import new


names_01=list(["MJY", "man", "xining"])
new_array=[None,None,None]
new_array1=[[1,2,3],[4,5,6]]
id_address=id(new_array1)
if  __name__=="__main__":
  print(type(names_01))
  print(type(new_array) )
  print(new_array1)
  print(1 in [1,2,3,4])
  print (max([1,2,3,4]))
  print (min(["5","6","3.14"]))
  print(min(["hello World"]))
  print([])
  print(bool([]))
  print(len(new_array1))
  print(len(new_array))
  print(id_address)