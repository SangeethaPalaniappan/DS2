#Need to write function for the distance searching


class Node:
    def __init__(self,val,key):
        
        self.edge=val
        self.data=key
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insert(self,src,dest,key):
        d=Node(dest,key)
        if a[src]==None:
            self.head=d
            a[src]=d
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=d    
    def delete(self,src,dest,key):
        if a[src]==None:
            print("There is no edge from",src,"to",dest)
        else:
            
            temp=self.head
            if temp.data==key:
                self.head=temp.next
                
                a[src]=temp.next
                temp.next=None
            else:
                while temp.next!=None:
                    if temp.next.data==key:
                        temp.next=temp.next.next
                        break
                    temp=temp.next    
                else:
                    print("There is no edge from",src,"to",dest)

    def search(self,src,dest,key):
        if a[src]==None:
            print("There is no edge from",src,"to",dest)
        else:
            temp=self.head
            while temp!=None:
                if temp.data==key:
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
            print(src,"-->",end="")
            while temp!=None:
                print("\t",temp.edge,"[",temp.data,"]",end=" ")
                temp=temp.next
            
                    
a=[None]*5
#a[0]=Node(1) 
#a[1]=Node(0)
#a[2]=Node(0)
#a[3]=Node(2)
#a[4]=Node(1)  
s=Linkedlist()

s.insert(0,1,5)
s.insert(0,2,7)
s.insert(0,3,9)
s.insert(0,4,11)
s.delete(0,1,5)
s.delete(0,3,8)
s.search(0,4,11)
s.search(0,2,11)
s.printg(0)

print("\n")
L=Linkedlist()
L.insert(1,0,4)
L.insert(1,2,2)
L.insert(1,3,6)
L.insert(1,4,12)
L.delete(1,0,2)
L.delete(1,0,4)
L.delete(1,4,4)
L.search(1,3,6)
L.printg(1)

print("\n")
M=Linkedlist()
M.insert(2,0,4)
M.insert(2,1,5)
M.insert(2,3,7)
M.insert(2,4,8)
M.delete(2,0,3)
M.delete(2,0,4)
M.insert(2,1,4)
M.search(2,9,5)
M.search(2,3,5)
M.printg(2)

print("\n")

D=Linkedlist()
D.insert(3,0,4)
D.insert(3,1,3)
D.insert(3,2,3)
D.insert(3,4,3)
D.delete(3,0,4)
D.delete(3,0,6)
D.printg(3)

print("\n")
L.delete(4,0,3)
L.search(4,5,2)
L.printg(4)

print("\n")