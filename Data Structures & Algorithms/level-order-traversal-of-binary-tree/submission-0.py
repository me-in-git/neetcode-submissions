# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        q=deque()
        q.append(root)
        res=[[root.val]]
        while q:
            l=len(q)
            arr=[]
            for i in range(l):
                el=q.popleft()
                if el.left:
                    q.append(el.left)
                    arr.append(el.left.val)
                if el.right:
                    q.append(el.right)
                    arr.append(el.right.val)
            if arr:
                res.append(arr)
            
        return res





        