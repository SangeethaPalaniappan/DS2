#Search in Binary Search Tree

class Node:
    def __init__(self,val):
        self.left=None
        self.data=val
        self.right=None

def Insert(root,key): 
    temp=root   
    if temp==None:
        newnode=Node(key)
        root=newnode
        return root
    elif temp.data<key:
        if temp.right!=None:
           Insert(temp.right,key)
        else:   
           newnode=Node(key)
           temp.right=newnode
        return root    
    elif temp.data>key:
        if temp.left!=None:
           Insert(temp.left,key)
        else:          
           newnode=Node(key)
           temp.left=newnode
        return root    
    else:
        print("Duplicate elements are not allowed")            
        return root          

                  
def Search(root,val):
    if val<root.data:
        temp=root.left
        if temp!=None:
            return Search(temp,val)
        else:
            return 0
               
    elif val>root.data:
        temp=root.right
        if temp!=None:
            return Search(temp,val)
        else:
            return 0      
    elif root.data==val:
        return 1
    
    else:
        return 0
                     
root=None
root=Insert(root,20)
root=Insert(root,50)
root=Insert(root,10)
root=Insert(root,20)
root=Insert(root,50)
root=Insert(root,15)
root=Insert(root,15)
root=Insert(root,25)
root=Insert(root,150)
root=Insert(root,100)
if Search(root,20)==1:
    print("Element found")
else:
    print("Element Not found")