class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j))
        while q:
            a,b =q.popleft()
            dirn=[[1,0],[0,1],[-1,0],[0,-1]]
            for dr,dc in dirn:
                nr,nc=a+dr,b+dc
                if nr in range(0,rows) and nc in range(cols):
                    if grid[nr][nc]==2147483647:
                        grid[nr][nc]= grid[a][b]+1
                        q.append((nr,nc))
                        
                            
                    
                                
                    
            
                
        
            
        
            

        