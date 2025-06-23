import sys
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dclinkedlist:
    def __init__(self):
        self.head=None
        self.last=None
    def display(self):
        if(self.head==None):
            print("Empty list")
        else:
            first=self.head
            while first is not None:
                if first.data is not None:
                    print(first.data,end=' ')
                first=first.next
                if(first==self.head):
                    break

    def atstart(self,newdata):
        temp=node(newdata)
        if(self.head==None):    
            self.head=temp
            self.last=temp
        else:
            temp.next=self.head
            temp.prev=self.head
            self.head=temp
    def atend(self,newdata):
        temp=node(newdata)
        if(self.head==None):
            self.head=temp
            self.last=temp
        else:
            self.last.next=temp
            temp.prev=self.last
            temp.next=self.head
            self.last=temp

    def inmid(self,key,newdata):
        temp=node(newdata)
        var=self.head
        while(var.data!=key and var.next!=self.head):
            var=var.next
        if(var==None):
            print("KEY NOT PRESENT")
        else:
            t=var.next
            var.next=temp
            temp.prev=var
            temp.next=t
            t.prev=temp

    def removenode(self,removekey):
        flag=0 #data not identified
        headval=self.head
        if(headval is not None):
            if(headval.data==removekey):  #headnode is deleting
                flag=1
                headval.data=None
                headval=headval.next
                self.head=headval
                return
            else:
                while(headval is not None):         
                    if(headval.data==removekey):
                        flag=1
                        break
                    if(headval.next==self.head):
                        break
                    prev=headval
                    headval=headval.next
        if(flag==0):
            print("data not found")
            return
        if(flag==1):   
            if(headval==None):
                return 
            prev.next=headval.next
            headval=None
s1=dclinkedlist()
s1.atstart(5)
s1.display()
print()
s1.atend(15)
s1.display()
print()
s1.inmid(10,50)
s1.display()
print()
s1.removenode(50)
s1.display()
print()
s1.removenode(3)
s1.display()
print()
s1.removenode(5)  
s1.display()
print()
        
        