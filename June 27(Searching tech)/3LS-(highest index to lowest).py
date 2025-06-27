# linear search from n-1 to 0 index

def rls(x,i,key):
    if(x[i]==key):
        return i
    if(i==0):              #
        return -1
    return rls(x,i-1,key)  #

import numpy as np
n=int(input()) 
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    d=int(input())
    x[i]=d
print(x)
key=int(input())
ans=rls(x,n-1,key)          #
if ans== -1:
    print("Data not present")
else:
    print(ans)