#Insertion in Binary Search Tree

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