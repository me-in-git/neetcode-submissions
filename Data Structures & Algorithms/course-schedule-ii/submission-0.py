class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:

        adj=[[] for _ in range(n)]

        for a,b in p:
            adj[b].append(a)
        
        visited=[0]*n
        stack=[]

        def dfs(i):
            visited[i]=1
            for nbr in adj[i]:
                if not visited[nbr]:
                    if dfs(nbr):
                        return True
                elif visited[nbr]==1:                    
                    return True
            
            stack.append(i)
            visited[i]=2
            return False

        for i in range(n):
            if not visited[i]:
                if dfs(i):
                    return []
            
        return stack[::-1]
        


            
