# BINEARY SEARCH - Arrange data in descending order:

n=int(input()) 
x=list(map(int,input().split(' ',n-1)))
print(x)
x.sort(reverse=True)    #descending order
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
        flag=1  
        break
    elif key>=x[mid]:
        high=mid-1      #
    else:
        low=mid+1       #
if(flag==0):
    print("Data not present")   
