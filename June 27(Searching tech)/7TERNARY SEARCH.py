# TERNARY SEARCH

n=int(input())   #size
x=list(map(int,input().split(' ',n-1)))
print(x)
x.sort()  
print(x)
key=int(input())
flag=0
l=0
r=n-1
while l<=r:
    print(l,r)
    mid1=l+(r-l)//3
    mid2=r-(r-l)//3
    print(mid1,mid2)
    if(x[mid1]==key):
        flag=1
        print(mid1)
        break
    elif(x[mid2]==key):
        flag=1
        print(mid2)
        break
    elif(key<x[mid1]):
        r=mid1-1
    elif(key>x[mid2]):
        l=mid2+1
    else:
        l=mid1+1
        r=mid2-1
if flag==0:
    print("data not found")
