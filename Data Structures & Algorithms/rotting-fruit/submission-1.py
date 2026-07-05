class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh+=1

        minutes=0
        dirn=[[0,1],[1,0],[-1,0],[0,-1]]

        while q and fresh>0:            
            minutes+=1

            for x in range(len(q)): #there has to be a for loop 
                r,c = q.popleft()
                for a,b in dirn:
                    
                    nr,nc= r+a,c+b
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))
        
        if fresh>0:
            return -1
            
        return minutes