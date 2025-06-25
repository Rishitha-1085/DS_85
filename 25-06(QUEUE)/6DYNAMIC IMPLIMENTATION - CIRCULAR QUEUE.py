# DYNAMIC IMPLIMENTATION - CIRCULAR QUEUE

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
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
            newnode.next=self.front     #

    def delete(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front==self.rear:
            x=self.front.data
            self.front.data=''   #
            self.front = None  
            self.rear = None 
        else:
            x= self.front.data
            self.front.data=''    #
            self.front = self.front.next
            return x

    def display(self):
        if self.front is None:
            print("Empty")
        temp = self.front
        while temp:
                print(temp.data, end=' ')
                temp = temp.next
                if(temp==self.front):
                    break
        print()


q1=CircularQueue()
while True:
    print('add<value>')
    print('delete')
    print('display')
    print('quit')
    do=input('What would you like to do? ').split()

    operation=do[0].strip().lower()
    if operation=='add':
        q1.add(int(do[1]))
    elif operation=='delete':
        deleted=q1.delete()
        if deleted is None:
            print('queue is Empty.')
        else:
            print('deleted value: ', int(deleted))
    elif operation=='display':
        q1.display()
    elif operation=='quit':
        break
