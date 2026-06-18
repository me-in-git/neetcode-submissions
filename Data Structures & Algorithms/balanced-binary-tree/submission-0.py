# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.c=1

        def bal(root):
            if root is None:
                return 0
            l=bal(root.left)
            r=bal(root.right)
            if abs(r-l)>1:
                self.c=0
                return -1
            h=max(l,r)+1
            return h
        
        bal(root)
        return self.c==1