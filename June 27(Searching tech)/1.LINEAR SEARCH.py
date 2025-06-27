# SEARCHING- LINEAR SEARCH

import numpy as np
n=int(input())   #size
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    d=int(input())
    x[i]=d
print(x)
key=int(input())
flag=0
#search
for i in range(n):
    if x[i]==key:
        print(i)
        flag=1 #data indentified
        break
    i+=1
if(flag==0):
    print("Data not present")
