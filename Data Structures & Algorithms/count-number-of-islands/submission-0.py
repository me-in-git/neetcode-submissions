class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def islands(x,y,grid):
            if x<0 or x>=rows or y<0 or y>=cols or grid[x][y]!='1':
                return 
            grid[x][y]='0'
            for dr,dc in directions:
                islands(x+dr,y+dc,grid)
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        rows=len(grid)
        cols=len(grid[0])
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    islands(i,j,grid)
                    count+=1
        return count

        

                        
            
                


        