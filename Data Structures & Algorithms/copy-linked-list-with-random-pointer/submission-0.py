"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return 

        h={}
        
        def copy(head):
            if not head:
                return
            
            if head not in h:
                newnode=Node(head.val)
                h[head]=newnode
            else:
                return h[head]

            h[head].next=copy(head.next)
            h[head].random=copy(head.random)

            return newnode
        
        copy(head)
        
        return h[head]


        