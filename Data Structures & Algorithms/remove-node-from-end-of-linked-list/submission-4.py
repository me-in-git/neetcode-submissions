# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng=0
        root=head
        while root:
            root=root.next
            leng+=1 

        if n==leng:
            return head.next            
        root=head
        tobe=leng-n

        while tobe>1:
            root=root.next
            tobe-=1

        if root.next.next:
            root.next=root.next.next
        else:
            root.next=None
        return head