# BINARY SEARCH-USING RECURSION

def rbs(x,l,h,key):
    if l<=h:
        print(l,h)
        mid=(l+h)//2     
        if x[mid] == key:
            return mid
        elif key>x[mid]:
            return rbs(x, mid + 1, h, key)
        else:
            return rbs(x, l, mid - 1, key)
    return -1
n=int(input())   
x=list(map(int,input().split(' ',n-1)))
print(x)
x.sort()
print(x)
key=int(input())
low=0
high=n-1
ans= rbs(x,low,high, key)
if ans== -1:
    print("Data not present")
else:
    print(ans)
