#have written code for deleting the leaf node
#Deletion in Binary Search Tree

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

def Delete(root,val):
        #Deleting the child node 
        if val>root.data:
           temp=root
           root=root.right 
           if root!=None:    
              if root.data==val:
                  if temp.right.right==None and temp.right.left==None:
                      temp.right=None
                      root=None
                      return temp
                  #else - other two conditions   
              Delete(root,val)
              return temp
           else:
               print("There is no element",val)
        elif val<root.data:  
           temp=root
           root=root.left 
           if root!=None:
               if root.data==val:
                   if temp.left.right==None and temp.left.left==None:
                      temp.left=None
                      root=None
                      return temp
                   #else - other two conditions   
               Delete(root,val) 
               return temp    
           else:
               print("There is no element",val) 
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
print("Deleting the leaf node")
root=Delete(root,15) 
root=Delete(root,15)  