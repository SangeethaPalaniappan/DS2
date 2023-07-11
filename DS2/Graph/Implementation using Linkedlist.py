class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insert(self,src,dest):
        d=Node(dest)
        if a[src]==None:
            self.head=d
            a[src]=d
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=d    
    def delete(self,src,dest):
        if a[src]==None:
            print("There is no edge from",src,"to",dest)
        else:
            
            temp=self.head
            if temp.data==dest:
                self.head=temp.next
                
                a[src]=temp.next
                temp.next=None
            else:
                while temp.next!=None:
                    if temp.next.data==dest:
                        temp.next=temp.next.next
                        break
                    temp=temp.next    
                else:
                    print("There is no edge from",src,"to",dest)

    def search(self,src,dest):
        if a[src]==None:
            print("There is no edge from",src,"to",dest)
        else:
            temp=self.head
            while temp!=None:
                if temp.data==dest:
                    print("Edege Found")
                    break
                temp=temp.next 
            else:
                print("No Edge Found")
                    
    def printg(self,src):
        temp=self.head
        if a[src]==None:
            print("There is no edge from",src)
        else:
            print(src,"-->",end=" ")
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
            
                    
a=[None]*5
#a[0]=Node(1) 
#a[1]=Node(0)
#a[2]=Node(0)
#a[3]=Node(2)
#a[4]=Node(1)  
s=Linkedlist()

s.insert(0,1)
s.insert(0,2)
s.insert(0,3)
s.insert(0,4)
s.delete(0,1)
s.delete(0,3)
s.search(0,4)
s.printg(0)

print("\n")
L=Linkedlist()
L.insert(1,0)
L.insert(1,2)
L.insert(1,3)
L.insert(1,4)
L.delete(1,0)
L.delete(1,0)
L.delete(1,4)
L.search(1,3)
L.printg(1)

print("\n")
M=Linkedlist()
M.insert(2,0)
M.insert(2,1)
M.insert(2,3)
M.insert(2,4)
M.delete(2,0)
M.delete(2,0)
M.insert(2,1)
M.search(2,9)
M.printg(2)

print("\n")

D=Linkedlist()
D.insert(3,0)
D.insert(3,1)
D.insert(3,2)
D.insert(3,4)
D.delete(3,0)
D.delete(3,0)
D.printg(3)

print("\n")
L.delete(4,0)
L.search(4,5)
L.printg(4)

print("\n")