# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        res=[]


        q=deque()
        q.append(root)

        while q:
            n=len(q)          
            
            
            for i in range(n):
                el=q.popleft()
                last=el.val

                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            
            res.append(last)
        
        return res           
                
