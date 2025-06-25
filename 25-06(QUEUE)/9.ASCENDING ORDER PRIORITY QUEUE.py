# PRIORITY QUEUE:
# ASCENDING ORDER PRIORITY QUEUE(pq)  - highest priority data(low value) is deleted

class pq:
    def __init__(self): 
        self.q=[]
        self.a=0  #counting items
    def add(self,newdata):
        self.q.append(newdata)
        print(self.q)
        self.a+=1
    def delete(self):
        minv=min(self.q)        
        mini=self.q.index(minv)
        del self.q[mini]
        print("DELETED DATA= ",minv)
        print(self.q)
        self.a-=1


p1=pq()
p1.add(12)
p1.add(1)
p1.add(14)
p1.add(17)  
while p1.a: 
    p1.delete()
