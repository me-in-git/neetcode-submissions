# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxii=0
        
        def maxd(root):
            if root is None:
                return 0
            l=maxd(root.left)
            r=maxd(root.right)
            self.maxii=max(self.maxii,(l+r+1))

            
            return max(l,r)+1
        
        maxd(root)
        return self.maxii -1


