# stack-Dynamic Implementation:using single linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class stack:
    def __init__(self):
        self.top=None  
    def push(self,newdata):
        newnode=node(newdata)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.top is None:
            print("EMPTY")
        else:
            x=self.top.data
            self.top=self.top.next
            return x
        
    def display(self):
        if self.top is None:
            print("EMPTY")
        else:
            temp=self.top
            while(temp):
                print(temp.data,end=' ')
                temp=temp.next
            print()

s1=stack()
s1.top=node(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
