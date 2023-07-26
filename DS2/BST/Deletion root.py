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
        
    elif temp.data<key:#if the root node is less than the key
        
        #if there is element in the right child
        if temp.right!=None:
           Insert(temp.right,key)#assigning the right node as root
           
        #if there is no element in the right child
        else:   
           newnode=Node(key)
           temp.right=newnode
        return root
        
    elif temp.data>key:#if the root node is greater than the key
        
        #if there is element in the left child
        if temp.left!=None:
           Insert(temp.left,key)#assigning the left node as root
           
        #if there is no element in the left child
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
        #If the value is greater than root go right 
        if val>root.data:
            
            #here I assinged temp because the next element cannot
            #have address of the previous element i.e.,root
           temp=root
           root=root.right 
           if root!=None:    
              if root.data==val:
                  #if it is the leaf node
                  if root.right==None and root.left==None:
                      temp.right=None
                      
                      return temp
                  #else - other two conditions 
                  
                  #if there is only one child
                  #either left child
                  elif root.right==None:
                      
                      #making the root's (the element to be deleted)left as root
                      
                      root=root.left
                      temp.right=root  
                      return temp
                      
                      
                    #or right child  
                  elif root.left==None:
                      
                      #making the root's (the element to be deleted)right as root
                      
                      root=root.right
                      temp.right= root 
                      return temp
                      
                      
                    #if the root to be deleted have two children  
                  else:
                      
                      #here these assignings are to arrange the node and it's children
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
                     
              Delete(root,val)#Recurse until we get the key 
              return temp
           else:
               print("There is no element",val)
               return temp
        
        
        #If the value is less than root go left 
        elif val<root.data: 
            
            #here I assinged temp because the next element cannot
            #have address of the previous element i.e.,root
           temp=root
           root=root.left 
           if root!=None:
               if root.data==val:
                   if root.right==None and root.left==None:
                      temp.left=None
                      root=None
                      return temp
                   #else - other two conditions 
                   
                   #if there is only one child
                  #either left child
                   elif root.right==None:
                       
                    #making the root's (the element to be deleted)left as root
                      root=root.left
                      temp.left=root  
                      return temp
                      
                #or right child      
                   elif root.left==None:
                       
                    #making the root's (the element to be deleted)right as root   
                      root=root.right
                      temp.left=root  
                      return temp  
                      
                    #if the root to be deleted have two children  
                   else:
                       
                       #here these assignings are to arrange the node and it's children
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
               return temp
        #if the root to be deleted 
        else:
            
            if root==None:
                print("No BST")
                return root
            elif root.data==val:
                if root.right==None and root.left==None:    
                    root=None
                elif root.right==None:
                     #here these assignings are to arrange the node and it's children
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
                        
                      Root=S
                    #if root.left!=None:
                          #root=root.left
                        #I have written the above statement but I don't know for what  
                            
                      Root.right=Right
                      Root.left=Left
                      
                      return Root   
                elif root.left==None:
                     #here these assignings are to arrange the node and it's children
                      Root=root
                      Right=root.right
                      Left=root.left
                      root=root.right
                      
                      while root.left!=None:
                        if root.left.left==None:
                            
                            if root.left.right!=None:
                                S=root.left
                                root.left=root.left.right
                                break 
                            else:
                                S=root.left
                                root.left=None
                                break
                        root=root.left
                      Root=S
                    #if root.left!=None:
                          #root=root.left
                        #I have written the above statement but I don't know for what  
                            
                      Root.right=Right
                      Root.left=Left
                      
                      return Root    
                #To delete the root node    
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
root=Insert(root,430)
root=Insert(root,250)
root=Insert(root,700)
root=Insert(root,90)


if Search(root,20)==1:
    print("Element found")
else:
    print("Element Not found")
print("Deleting the leaf node")
root=Delete(root,40)
print("Deleting the node with one child")
root=Delete(root,30)
root=Delete(root,50)
root=Delete(root,50)