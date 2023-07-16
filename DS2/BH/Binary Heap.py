#Need to write Binary Heap


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
                      
                      return temp
                  #else - other two conditions  
                  elif root.right==None:
                      root=root.left
                      temp.right=root  
                      return temp
                  elif root.left==None:
                      root=root.right
                      temp.right= root 
                      return temp
                  else:
                      Root=root
                      Right=root.right
                      Left=root.left
                      root=root.left
                      
                      while root.right!=None:
                        if root.right.right==None:
                            #if there is a left child of the root.right then 
                            if root.right.left!=None:
                                S=root.right
                                root.right=root.right.left
                                break 
                           #if there is a no child or it is the leaf node of the root.right then
                            else:
                                S=root.right
                                root.right=None
                                break
                        root=root.right
                      Root=S
                      '''if root.left!=None:
                          root=root.left''' 
                        #I have written the above statement but I don't know for what  
                      Root.right=Right  
                      Root.left=Left
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
                      Right=root.right
                      Left=root.left
                      root=root.left
                      
                      while root.right!=None:
                        if root.right.right==None:
                            
                            if root.right.left!=None:
                                S=root.right
                                root.right=root.right.left
                                break 
                            else:
                                S=root.right
                                root.right=None
                                break
                        root=root.right
                      Root=S
                    #if root.left!=None:
                          #root=root.left
                        #I have written the above statement but I don't know for what  
                            
                      Root.right=Right
                      Root.left=Left
                      temp.left=Root
                      return temp     
                        
                        
               Delete(root,val) 
               return temp    
           else:
               print("There is no element",val) 
        else:
            
            if root==None:
                print("No BST")
            elif root.data==val:
                if root.right==None and root.left==None:    
                    root=None
                elif root.right==None:
                    Root=root.left
                    root=None
                elif root.left==None:
                    Root=root.right
                    root=None
                    
                else:
                    
                    temp=root      
                    Root=root
                    Right=root.right
                    Left=root.left
                    root=root.left
                    
                    while root.right!=None:
                        if root.right.right==None:    
                            if root.right.left!=None:
                                S=root.right
                                root.right=root.right.left
                                break 
                            else:
                                S=root.right
                                root.right=None
                                break
                        root=root.right
                    else:
                        S=root
                        Root=S
                        temp=None
                    
            
                    if temp!=None:
                        Root=S
                        Root.left=Left
                        Root.right=Right
                    
                    temp=None
                return Root
            
root=None
root=Insert(root,50)
root=Insert(root,40)
root=Insert(root,30)
root=Insert(root,43)
root=Insert(root,25)
root=Insert(root,70)
root=Insert(root,90)



if Search(root,20)==1:
    print("Element found")
else:
    print("Element Not found")
print("Deleting the leaf node")
root=Delete(root,90)
print("Deleting the node with one child")
root=Delete(root,70)
root=Delete(root,50)
root=Delete(root,50)