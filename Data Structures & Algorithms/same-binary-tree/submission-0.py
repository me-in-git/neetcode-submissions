# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def same(r1,r2):
            if r1 is None and r2 is None:
                return True
            if (not r1 and r2) or (not r2 and r1):
                return False            
            l=same(r1.left,r2.left)
            r=same(r1.right,r2.right)
            if r1.val==r2.val:
                return l and r
            else:                
                return False

        return same(p,q)