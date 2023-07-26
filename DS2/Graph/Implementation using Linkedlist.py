#Need to write function for the distance searching -completed
#Need to search which is the shortest distance
#Need to search the vertex - not to change the name of the vertex

class Node:
    def __init__(self,val,key):
        
        self.edge=key
        self.gver=val
        self.next=None
    
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insert(self,src,dest,key):#inserting the edge
        d=Node(dest,key)
        
        if a[src]==None:#if there is no edge from the vertex
            self.head=d
            a[src]=d
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=d    
            
    def delete(self,src,dest,key):#deleting the edge
    
        if a[src]==None:#if there is no edge from the vertex
            print("There is no edge of weight",key," from",src,"to",dest)
        
        else:
            temp=self.head
            #to check whether the dest vertex is same or not
                #else it will delete the edge of the given weight of any other vertex
            
            #Iterating to get the vertex to be deleted
            while temp.gver!=dest:
                temp=temp.next
                if temp==None:
                    print("There is no edge of weight",key," from",src,"to",dest)
                    return
            if  temp.edge==key:
                self.head=temp.next
            
                a[src]=temp.next
                temp.next=None
                return
            else:
                while temp.next!=None:
                    #even we found the vertex
                    #It is necessary to check the vertex because
                    #here I'm checking the temp's next so need to check the vertex and key
                    
                    if temp.next.gver==dest and temp.next.edge==key:
                        temp.next=temp.next.next
                        break
                    temp=temp.next    
                else:
                    print("There is no edge of weight",key," from",src,"to",dest)
                    return
            
            print("There is no edge of weight",key,"from",src,"to",dest)

    def search(self,src,dest,key):#searching the edge
        if a[src]==None:
            print("There is no edge from",src,"to",dest)
        else:
            temp=self.head
            while temp!=None:
                #to check whether the dest vertex is same or not
                #else it will delete the edge of the given weight of any other vertex
                if temp.gver==dest:
                    if temp.edge==key:
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
                print("\t",temp.gver,"[",temp.edge,"]",end=" ")
                temp=temp.next
    def vertexsearch(self,size,ver):
        if ver>=size:
            print("There is no vertex")
        else:
            print("Vertex found")             
size=int(input("s"))                    
a=[None]*size
#a[0]=Node(1) 
#a[1]=Node(0)
#a[2]=Node(0)
#a[3]=Node(2)
#a[4]=Node(1) 
#why seperated functions were written?
s=Linkedlist()

#else I can create a function for calling insert,delete and search 
'''def func_insert():
    n=int(input("No.of insertions:"))
    for x in range(n):
        ver1=int(input("ver1:"))
        ver2=int(input("ver2:"))
        edge=int(input("edge:"))
        insert(ver1,ver2,edge)
        
def funct_delete():
    n=int(input("No.of deletions:"))
    for x in range(n):
        ver1=int(input("ver1:"))
        ver2=int(input("ver2:"))
        edge=int(input("edge:"))
        delete(ver1,ver2,edge)'''
s.insert(0,1,5)
s.insert(0,2,7)
s.insert(0,3,9)
s.insert(0,4,11)
s.delete(0,1,5)
s.delete(0,3,8)
s.search(0,4,11)
s.search(0,2,11)
s.printg(0)

s.insert(1,0,4)
s.insert(1,2,2)
s.insert(1,3,6)
s.insert(1,4,12)
s.delete(1,0,2)
s.delete(1,0,4)
s.delete(1,4,4)
s.search(1,3,6)
s.printg(1)


s.insert(2,0,4)
s.insert(2,1,5)
s.insert(2,3,7)
s.insert(2,4,8)
s.delete(2,0,3)
s.delete(2,0,4)
s.insert(2,1,4)
s.search(2,9,5)
s.search(2,3,5)
s.printg(2)

s.insert(3,0,4)
s.insert(3,1,3)
s.insert(3,2,3)
s.insert(3,4,3)
s.delete(3,0,4)
s.delete(3,0,6)
s.printg(3)


s.delete(4,0,3)
s.search(4,5,2)
s.printg(4)
s.vertexsearch(size,2)
s.vertexsearch(size,7)
#adding the vertex
a.append(None)

#deleting the vertex
del(a[2])#2 is the position

