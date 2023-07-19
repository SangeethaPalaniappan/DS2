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
        
def Insert(i,val,arr):
    a=Index(arr)
    left=(2*i)+1
    right=left+1
    if arr[i]==None:
        arr[i]=val
        return arr
    else:
        if arr[left]==None:
            arr[left]=val
            return arr
        elif arr[right]==None:
            arr[right]=val
            return arr


a=[]
size=len(a)

if size!=0:
    i=size-1
else:
    i=0
a=Insert(i,50,a)
size=len(a)
if size!=0:
    i=size-1
else:
    i=0
a=Insert(i,40,a)
size=len(a)
if size!=0:
    i=(size-1)//2
else:
    i=0
a=Insert(i,30,a)
size=len(a)
if size!=0:
    i=(size-1)//2
else:
    i=0
a=Insert(i,20,a)
size=len(a)
if size!=0:
    i=(size-1)//2
else:
    i=0
a=Insert(i,10,a)


