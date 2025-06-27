
# TERNARY SEARCH - RECURSION

def rts(x,l,r,key):
    if l<=r:
        print(l,r)
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        print(mid1,mid2)
        if(x[mid1]==key):
            return mid1
        elif(x[mid2]==key):  
            return mid2
        elif(key<x[mid1]):    
            return rts(x,l,mid1-1,key)
        elif(key>x[mid2]):    
            return rts(x,mid2+1,r,key)
        else:
            return rts(x,mid1+1,mid2+1,key)                  
    return -1
n=int(input())   #size
x=list(map(int,input().split(' ',n-1)))
print(x)
x.sort()  
print(x)
key=int(input())
l=0
r=n-1
ans=rts(x,l,r,key)  #calling function
if ans== -1:
    print("Data not present")
else:
    print(ans)