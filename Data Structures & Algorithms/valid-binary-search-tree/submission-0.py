# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.c=1

        def check(root,mini,maxi):
            if root is None or self.c==0:
                return 
            if mini< root.val< maxi:
                pass
            else:
                self.c=0
                

            check(root.left,mini,root.val)
            check(root.right,root.val,maxi)
    
        check(root,float("-inf"),float("inf"))
        return self.c==1


        