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
    if val>arr[i]:
        temp=arr[i]
        arr[pos]=temp
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
    
    

        
def Insert(i,val,arr):#i is the parent node
    a=Index(arr)
    left=(2*i)+1
    right=left+1
    if arr[i]==None:
        arr[i]=val
        return arr
    else:
        if arr[left]==None:
            arr[left]=val
            Swap(i,arr,val,left)
            return arr
        elif arr[right]==None:
            arr[right]=val
            Swap(i,arr,val,right)
            return arr
def Size(size):
    if size!=0:
        i=(size-1)//2
        return i
    else:
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
            if arr[i]<arr[left] or arr[i]<arr[right]:
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
def delete(arr):
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

def Heapify(arr,i,size):
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