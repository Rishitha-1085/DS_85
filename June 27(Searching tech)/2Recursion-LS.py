# LINEAR SEARCH - USING RECURSION

def rls(x,i,key):
    if(x[i]==key):
        return i
    if(len(x)-1 ==i):
        return -1 #data not found
    return rls(x,i+1,key)

import numpy as np
n=int(input())   #size
x=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    d=int(input())
    x[i]=d
print(x)
key=int(input())
ans=rls(x,0,key)   #calling function
if ans== -1:
    print("Data not present")
else:
    print(ans)