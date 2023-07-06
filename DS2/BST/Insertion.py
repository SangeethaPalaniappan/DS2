#Insertion in Binary Search Tree

class Node:
    def __init__(self,val):
        self.left=None
        self.data=val
        self.right=None


def Insert(root,key):   
    if root==None:
        newnode=Node(key)
        root=newnode
        return root
    elif root.data<key:
        if root.right!=None:
           Insert(root.right,key)
        else:   
           newnode=Node(key)
           root.right=newnode
        return root    
    elif root.data>key:
        if root.left!=None:
           Insert(root.left,key)
        else:          
           newnode=Node(key)
           root.left=newnode
        return root    
    else:
        print("Duplicate elements are not allowed")            
        return root          
                  

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