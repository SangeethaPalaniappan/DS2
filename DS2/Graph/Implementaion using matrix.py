class matrix:
    def __init__(self,size):
        self.a=[]
        self.size=size
        for i in range(self.size):
            self.a.append([0 for x in range(self.size)])
            print(self.a[i])
        

    def addedge(self,start,end):
        
        if self.a[start][end]==0:
            self.a[start][end]=1
        else:
            print("There exist an edge")
    def removedge(self,start,end):
        if self.a[start][end]==1:
            self.a[start][end]=0
        else:
            print("There is no edge")
    def searchedge(self,start,end):
        if self.a[start][end]==1:
            print("Element found")
        else:
            print("No element found")
    def printedge(self,size):
        for x in range(size):
            for y in range(size):
                print(self.a[x][y],end=" ")
            print("\n")    

d=matrix(3)
d.addedge(0,1)
d.addedge(0,2)
d.addedge(2,1)
d.addedge(2,1)
d.removedge(0,0)
d.removedge(0,2)
d.removedge(2,1)
d.searchedge(0,1)
d.searchedge(1,2)
d.printedge(3)
