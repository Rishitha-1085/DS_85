# stack-Dynamic Implementation:using single linked list
# input from User
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

while True:
    print('push<value>')
    print('pop')
    print('display')
    print('quit')
    do=input('What would you like to do? ').split()

    operation=do[0].strip().lower()
    if operation=='push':
        s1.push(int(do[1]))
    elif operation=='pop':
        popped=s1.pop()
        if popped is None:
            print('Stack is Empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation=='display':
        s1.display()
    elif operation=='quit':
        break
