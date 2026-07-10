class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        

        if len(edges)!= n-1:
            return False   

        if n==1:
            return True            

        adj=[[] for i in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited= [False]*n

        def dfs(node, parent):
            visited[node]=True
            for n in adj[node]:
                if visited[n] == False:
                    if not dfs(n,node):
                        return False
                
                elif n!=parent:
                    return False
            
            return True

        if not dfs(0,-1):
            return False

        return all(visited)


        

