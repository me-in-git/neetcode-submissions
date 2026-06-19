# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.v=-1
        self.f=k

        def kth(root):
            if root is None or self.v!=-1:
                return
            kth(root.left)
            self.f-=1
            if self.f==0:
                self.v=root.val
            kth(root.right)
        
        kth(root)
        return self.v