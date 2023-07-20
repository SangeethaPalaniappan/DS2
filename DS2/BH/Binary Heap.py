#Need to write Binary Heap

'''
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


class Index:
    def __init__(self,a):
        self.m=a.append(None)
        
def Swap(i,arr,val,pos):
    if val>arr[i]:
        temp=arr[i]
        arr[pos]=temp
        arr[i]=val
         
        if i!=0:
            Swap((i-1)//2,arr,arr[i],i)
            left=(2*i)+1
            right=left+1
            if left<len(arr) and arr[left]>=arr[i]:
                Swap(pos,arr,val,left)
                if right<len(arr)and arr[right]>=arr[i]:
                    Swap(pos,arr,val,right)   
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

def delete(arr):
    c=len(a)
    temp=a[0]
    a[0]=a[c-1]
    a[c-1]=temp
    a.pop()
    return a
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

a=delete(a)

a=delete(a)

print("Parent of 221:",Parent(a,221))
print("Parent of 94:",Parent(a,94))
print("Parent of 75:",Parent(a,75))
print("Parent of 50:",Parent(a,50))

