class Solution:
    def canFinish(self, n: int, prq: List[List[int]]) -> bool:

        adj=[[] for i in range(n)]

        for a,b in prq:
            adj[b].append(a)


        def dfs(node):
            visited[node]=1
            for nbr in adj[node]:
                if visited[nbr]==1:                    
                        return True
                elif visited[nbr]==0:
                    if dfs(nbr):
                        return True
            
            visited[node]=2
            
            return False
        
        visited=[0]*n

        for i in range(len(visited)):
            if not visited[i]:
                if dfs(i):
                    return False
        
        return True


        
