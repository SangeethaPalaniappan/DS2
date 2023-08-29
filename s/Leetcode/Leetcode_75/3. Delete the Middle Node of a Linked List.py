# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next   
        s=count//2
        print(s)   
        temp=head 
        prev=temp 
        for i in range(s):
            prev=temp
            temp=temp.next
        if prev.next!=None:
            prev.next=temp.next
        
        else:
            return 
        return head 