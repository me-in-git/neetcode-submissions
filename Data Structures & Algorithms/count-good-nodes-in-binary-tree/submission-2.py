# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.c=0
        
        def good(root,maxval):
            if root is None:
                return
            
            if maxval<=root.val:
                self.c+=1
            
            good(root.left,max(maxval,root.val))
            good(root.right,max(maxval,root.val))
        
        good(root,float("-inf"))

        return self.c

        
            

