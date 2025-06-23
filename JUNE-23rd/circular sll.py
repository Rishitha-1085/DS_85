# CIRCULAR SINGLY LINKED LIST:

class node:       #node creation
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
        
class sclinkedlist:
    def __init__(self):
        self.headval=None
        
    def listprint(self):
        printval=self.headval
        while printval is not None:
            if(printval.dataval is not None):
                print(printval.dataval,end=' ')
            printval=printval.nextval
            if(printval==self.headval):           # 1000 == 1000 then break
                break
        print()
# INSERTION   
    def atstart(self,newdata):
        newnode=node(newdata)
        if self.headval is None:   #empty list
            newnode.nextval=newnode 
            self.headval=newnode
    
        else:
            newnode.nextval=self.headval
            self.headval=newnode
        
    def atend(self,newdata):
        newnode=node(newdata)
        if self.headval is None:
            newnode.nextval=newnode 
            self.headval=newnode
            
        else:
            temp=self.headval
            while(temp.nextval):
                temp=temp.nextval
                if(temp==self.headval):
                    break
            temp.nextval=newnode
            newnode.nextval=self.headval
        
        
    def inmid(self,middle,newdata):
        if middle is None:
            print("data not present")
            return
        else:
            newnode=node(newdata)
            temp=self.headval
            while(temp.dataval!=middle and temp.nextval!=self.headval):   
                temp=temp.nextval
            newnode.nextval=temp.nextval
            temp.nextval=newnode
# DELETION    
    def removenode(self,removekey):
        flag=0 #data not identified
        headval=self.headval
        if(headval is not None):
            if(headval.dataval==removekey):  #headnode is deleting
                flag=1
                headval.dataval=None
                headval=headval.nextval
                self.headval=headval
                return
            else:
                while(headval is not None):         
                    if(headval.dataval==removekey):
                        flag=1
                        break
                    if(headval.nextval==self.headval):
                        break
                    prev=headval
                    headval=headval.nextval
        if(flag==0):
            print("data not found")
            return
        if(flag==1):   
            if(headval==None):
                return 
            prev.nextval=headval.nextval
            headval=None
               
s1=sclinkedlist()
s1.headval=node("mon")
s1.atstart("sun")
s1.listprint()
s1.atend("thu")
s1.listprint()
s1.inmid("mon","tue")
s1.listprint()
s1.removenode("thu")
s1.listprint()
s1.removenode("sat")
s1.listprint()
s1.removenode("sun")  #??
s1.listprint()

