# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca=None
        self.c=0
        def lca(root):
            if root is None or self.c==1:
                return (False,False)
            
            (lp,lq)=lca(root.left)
            (rp,rq)=lca(root.right)
            pthere=root.val==p.val or lp or rp
            qthere=root.val==q.val or lq or rq
            if pthere and qthere and self.c==0:
                self.lca=root
                self.c=1
                return (True,True)
            return(pthere,qthere)
        
        lca(root)
        return self.lca
        
            
        