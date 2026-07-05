"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned={}
        if node is None:
            return
        
        def dfs(node):
            if node in cloned:
                return cloned[node]
            new=Node(node.val)
            cloned[node]=new
            for n in node.neighbors:
                new.neighbors.append(dfs(n))
            return new

    
        return dfs(node)