#Need to write Binary Heap

'''
#To work on linkedlist
class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None
        
        
def Insert(root,val):
    if root.data==None:
        root.data=val
    elif root.left==None:
        root.left.data=val
    elif root.right==None:
        root.right=val
    
    Insert(root,val)
    '''


'''class Index:
    def __init__(self,a):            #can also use this
        self.m=a.append(None)'''
def Index(a):
    m=a.append(None)
        
def Swap(i,arr,val,pos):
    #i-parent node
    #pos-either left or right index
    #val-the new element to be added
    if val>arr[i]:
        
        arr[pos]=arr[i]
        arr[i]=val
         
        if i!=0:
            Swap((i-1)//2,arr,arr[i],i)
            '''left=(2*i)+1
            right=left+1
            if left<len(arr) and arr[left]>=arr[i]:
                Swap(pos,arr,val,left)
                if right<len(arr)and arr[right]>=arr[i]:
                    Swap(pos,arr,val,right)'''   
    return arr    
    
    

    #Insert is the Bottom-up approach
    
def Insert(i,val,arr):#i is the parent node
    a=Index(arr)#adding the index at last
    left=(2*i)+1#left child index
    right=left+1#right child index
    
    if arr[i]==None:
        arr[i]=val
        return arr
    
    else:
        if arr[left]==None:
            arr[left]=val
            Swap(i,arr,val,left)#to check the value Binary heap property
            return arr
            
        elif arr[right]==None:
            arr[right]=val
            Swap(i,arr,val,right)#to check the value Binary heap property
            return arr

def Size(size):
    if size!=0:#here size the parent node 
        i=(size-1)//2
        return i
    else:#if the position is root 
        i=0
        return i

def Parent(arr,val):
    for x in arr:
        if val==x:
            break
    else:
        e="No Element in the list"
        return e
        
    v=arr.index(val)
    if v==0:
        r="It is the root node"
        return r
        #here no v>=size because the size is already fixed and 
        #if there is no value then v cannot exist
    else:
        p=(v-1)//2 #parent of the node
        m=arr[p]
        return m

def ChildNode(arr,val):
    for x in arr:
        if val==x:
            break
    else:
        print("No elements in the list")
        
    g=arr.index(val)
    
    left=(2*g)+1
    right=left+1
    if left>=len(arr):
        print("It is the leaf node")
    else:
        if left==len(arr)-1:
            print("It has only left child")
            print("leftchild:",arr[left])
        else:    
            print("leftchild:",arr[left])
            print("rightchild:",arr[right])
        


def dswap(i,arr):#i is the parent node
    left=(2*i)+1
    right=left+1
    if left<len(arr):
        temp=arr[i]
        if right==len(arr):#Having only left child 
            if arr[i]<arr[left]:
                arr[i]=arr[left]
                arr[left]=temp
            return arr
        else:
            if arr[i]<arr[left] or arr[i]<arr[right]:#to check the root node's children are greater than the parent
                #if the root node is lesser then check whhich child is greater
                if arr[left]<arr[right]:
                    arr[i]=arr[right]
                    arr[right]=temp
                    dswap(right,arr)
                else:
                    arr[i]=arr[left]
                    arr[left]=temp
                    dswap(left,arr)
            return arr
    elif left>=len(arr):
        return arr

##Delete is the Top-down approach
    
def delete(arr):
    #swaping the 1st and last  and delete the last element
    #after checking whether it satisfies the binary heap property
    c=len(arr)
    temp=a[0]
    arr[0]=arr[c-1]
    arr[c-1]=temp
    arr.pop()
    dswap(0,arr)
    return arr

def Heap(arr,size):
    l=size//2
    while l>=0:
        Heapify(arr,l,size)
        l-=1
    return arr    

def Heapify(arr,i,size):#to check the given array satisfies the BH property else heapify it
    left=(2*i)+1
    right=left+1
    temp=i
    
    if left<size and arr[temp]<arr[left]:
        temp=left
    if right<size and arr[temp]<arr[right]:
        temp=right
    if temp!=i:
        s=arr[temp]
        arr[temp]=arr[i]
        arr[i]=s
        
        Heapify(arr,temp,size)
a=[]
s=len(a)
i=Size(s)
a=Insert(i,50,a)

s=len(a)
i=Size(s)
a=Insert(i,40,a)

s=len(a)
i=Size(s)
a=Insert(i,30,a)

s=len(a)
i=Size(s)
a=Insert(i,20,a)

s=len(a)
i=Size(s)
a=Insert(i,75,a)

s=len(a)
i=Size(s)
a=Insert(i,94,a)

s=len(a)
i=Size(s)
a=Insert(i,103,a)

s=len(a)
i=Size(s)
a=Insert(i,221,a)

print("Child of 221:")
ChildNode(a,221)
print("Child of 20:")
ChildNode(a,20)
print("Child of 50:")
ChildNode(a,50)

a=delete(a)

a=delete(a)

print("Parent of 221:",Parent(a,221))
print("Parent of 94:",Parent(a,94))
print("Parent of 75:",Parent(a,75))
print("Parent of 50:",Parent(a,50))


a=[10,20,30,40,50,60]
a=Heap(a,len(a))

for i in a:
    print(i,end=" ")