class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj=[[] for _ in range(n)]


        def dfs(node):

            visited[node]=1

            for nbr in adj[node]:
                if not visited[nbr]:
                    dfs(nbr)
            
            return





        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited=[0]*n
        conn=0

        for i in range(len(visited)):
            if not visited[i]:
                dfs(i)
                conn+=1
        
        
        
        return conn
                
            



