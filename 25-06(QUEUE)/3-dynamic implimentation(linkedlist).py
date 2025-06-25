# DYNAMIC IMPLIMENTATION OF LINEAR QUEUE:
# SINGLE LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinearQueue:
    def __init__(self):
        self.front = None  
        self.rear = None  

    def add(self,newdata):
        newnode = Node(newdata)
        if self.front is None:
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def delete(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front==self.rear:
            x=self.front.data
            self.front = None  
            self.rear = None 
            return x
        else:
            x= self.front.data
            self.front = self.front.next
            return x

    def display(self):
        if self.front is None:
            print("Empty")
        temp = self.front
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


q=LinearQueue()
q.add(10)
q.add(20)
q.add(30)
q.display()  

q.delete()
q.display()      
q.delete()
q.delete()
q.display()     
