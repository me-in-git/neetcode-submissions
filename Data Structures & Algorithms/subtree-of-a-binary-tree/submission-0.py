# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.yes=0
        def check(root,subroot):
            if root is None and subRoot is None:
                return False
            if root is None or subRoot is None:
                return False
            
            check(root.left,subroot)
            check(root.right,subroot)
            if root.val==subRoot.val:
                if issubroot(root,subroot):
                    self.yes=1
                    return True 
            return False  

                

        def issubroot(p,q):     
            if not p and not q:
                return True      
            if not p and q or not q and p:
                return False
            if p.val!=q.val:
                return False

            return issubroot(p.left,q.left) and issubroot(p.right,q.right)
        
        check(root,subRoot)
        return self.yes==1