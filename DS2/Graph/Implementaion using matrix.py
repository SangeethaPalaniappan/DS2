#Need to write function for the nearest distance

class matrix:
    
    def __init__(self,size):
        self.a=[]
        self.size=size
        for i in range(self.size):
            self.a.append([0 for x in range(self.size)])
            print(self.a[i])
        

    def addedge(self,start,end,val):
        
        if self.a[start][end]==0:
            self.a[start][end]=val
        else:
            print("There exist an edge")
    
    def removedge(self,start,end,val):
        if self.a[start][end]==val:
            self.a[start][end]=0
        else:
            print("There is no edge")
    
    def searchedge(self,start,end,val):
        if self.a[start][end]==val:
            print("Edge found")
        else:
            print("No edge found")
    
    def printedge(self,size):
        for x in range(size):
            for y in range(size):
                print(self.a[x][y],end=" ")
            print("\n")    

size=int(input("s:"))
d=matrix(size)
print("\n\nAdding Edge:")
d.addedge(0,1,5)
d.addedge(0,2,6)
d.addedge(1,2,7)
d.addedge(2,1,2)
d.addedge(2,1,3)
print("\nprinting Edge:")
d.printedge(size)
print("\nRemoving Edge:")
d.removedge(0,0,3)
d.removedge(0,2,6)
d.removedge(2,1,5)
print("\n\nSearching Edge:")
d.searchedge(0,1,5)
d.searchedge(1,2,4)
print("\nPrinting Edge after deletion:")
d.printedge(size)
