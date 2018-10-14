class Node:
    def __init__(self,v=None):
        self.value=v
        self.next=None
    def isempty(self):
        if self.value==None:
            return(True)
        else:
            return (False)




    def append(self,v):
        if self.isempty():
            self.value=v
            return()
        temp=self
        while temp.next!=None:
            temp=temp.next
        newnode=Node(v)
        temp.next=newnode
        return()



    def insert(self,v):
        if self.isempty():
            self.value=v
            return
        newnode=Node(v)
        (self.value,newnode.value)=(newnode.value,self.value)
        (self.next,newnode.next)=(newnode,self.next)


    def delete(self,x):
        if self.isempty():
            return()
        if self.value==x:
            if self.next==None:
                self.value=None
            else:
                self.value=self.next.value
                self.next=self.next.next
        temp=self
        while temp.next!=None:
            if temp.next.value==x:
                temp.next=temp.next.next
                return()
            else:
                temp=temp.next
        return()

    def __str__(self):
        selflist=[]
        if self.value==None:
            return(str(selflist))
        temp=self
        selflist.append(temp.value)
        while temp.next!=None:
            temp=temp.next
            selflist.append(temp.value)
        return(str(selflist))


l=Node(1)
print(l)
l.append(2)
print(l)
l.delete(2)
print(l)
l.insert(24)
print(l)
