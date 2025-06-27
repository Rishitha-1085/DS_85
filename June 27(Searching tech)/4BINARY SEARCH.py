# BINARY SEARCH

n=int(input())   #size
x=list(map(int,input().split(' ',n-1)))
print(x)
x.sort()
print(x)
key=int(input())
flag=0
low=0
high=n-1
while low<=high:
    print(low,high)
    mid=(low+high)//2
    if x[mid]==key:
        print(mid)
        flag=1  #data indentified
        break
    elif key>=x[mid]:
        low=mid+1
    else:
        high=mid-1
if(flag==0):
    print("Data not present")   
