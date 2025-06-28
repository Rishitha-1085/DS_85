# MINIMUM SPANNING TREE:
# PRIMS ALGORITHM:

from numpy import *
m=int(input())  # no of vertices-m
n=m
x=[[int(input())for j in range(n)]for i in range(m)]   #x-matrix- nested list
arr=array(x)
print(arr)
INF=9999999
selectednode=zeros(m)
#selected_node=[0,0,0,0,0]
no_edge=0
selectednode[0]=True
ans=0
#printing for edge and weight
print("Edge : Weight\n")
while(no_edge<m-1):
    minimum=INF
    a=0
    b=0
    for x in range(m):
        if selectednode[x]:
            for y in range(m):
                if((not selectednode[y] and arr[x][y])):
                    #not in selected and there is an edge
                    if minimum>arr[x][y]:
                        minimum=arr[x][y]
                        a=x
                        b=y
    print(str(a)+"-"+str(b)+":"+str(arr[a][b]))
    ans=ans+minimum
    selectednode[b]=True
    no_edge+=1
print(ans)
