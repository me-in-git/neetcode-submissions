class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def maxarea(x,y):
            if x<0 or x>= rows or y<0 or y>=cols or grid[x][y]!=1:
                return 0
            grid[x][y]=0
            return (1 + maxarea(x + 1, y) + maxarea(x - 1, y) + maxarea(x, y + 1) + maxarea(x, y - 1))
        
        rows=len(grid)
        cols=len(grid[0])
        maxi=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    val=maxarea(i,j)
                    maxi=max(maxi,val)
        return maxi





