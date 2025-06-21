# SINGLE LINKEDLIST - Insertion of data at beginning,last,middle
class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class slinkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):     
        printval=self.headval
        while printval is not None:
            print(printval.dataval,end=' ')
            printval=printval.nextval
        print()
    def atbeg(self,newdata):       #Insertion of data
        newnode=node(newdata)
        if self.headval is None:
            self.headval=newnode
        newnode.nextval=self.headval
        self.headval=newnode

    def atend(self,newdata):
        newnode=node(newdata)
        if self.headval is None:
            self.headval=newnode
        last=self.headval
        while(last.nextval):
            last=last.nextval
        last.nextval=newnode   #null is replaced to newnode address

    def inmid(self,middle,newdata):
        if middle is None:
            print("Data not present")
        newnode=node(newdata)   #creating newnode
        temp=self.headval
        while(temp.dataval!=middle and temp.nextval!=None):    #it is not a last node
            temp=temp.nextval
        newnode.nextval=temp.nextval
        temp.nextval=newnode

s1=slinkedlist()
s1.headval=node("mon")
e2=node("tue")
e3=node("wed")
s1.headval.nextval=e2
e2.nextval=e3
s1.listprint()
s1.atbeg("sun")
s1.listprint()
s1.atend("thu")
s1.listprint()
s1.inmid("tue","fri")
s1.listprint()
