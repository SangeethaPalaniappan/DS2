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
                  if root.right==None and root.left==None:
                      temp.right=None
                      root=None
                      return temp
                  #else - other two conditions  
                  elif root.right==None:
                      root=root.left
                      temp.right=root  
                      return root
                  elif root.left==None:
                      root=root.right
                      temp.right= root 
                      return root
                  else:
                      Root=root
                      root=root.left
                      
                      while root.right!=None:
                         root=root.right
                      Root=root
                      temp.right=Root
                           
                      return temp     
                     
              Delete(root,val)
              return temp
           else:
               print("There is no element",val)
        elif val<root.data:  
           temp=root
           root=root.left 
           if root!=None:
               if root.data==val:
                   if root.right==None and root.left==None:
                      temp.left=None
                      root=None
                      return temp
                   #else - other two conditions 
                   elif root.right==None:
                      root=root.left
                      temp.left=root  
                      return temp
                   elif root.left==None:
                      root=root.right
                      temp.left=root  
                      return temp  
                   else:
                      Root=root
                      root=root.left
                      while root.right!=None:
                          root=root.right
                      Root=root
                      temp.left=Root
                      return temp     
                        
                        
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
root=Insert(root,17)
root=Insert(root,15)
root=Insert(root,25)
root=Insert(root,150)
root=Insert(root,100)

if Search(root,20)==1:
    print("Element found")
else:
    print("Element Not found")
print("Deleting the leaf node")
root=Delete(root,100)
print("Deleting the node with one child")
root=Delete(root,10)
root=Delete(root,50)