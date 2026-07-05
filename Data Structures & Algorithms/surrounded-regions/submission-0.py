class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        
        dirn=[[0,1],[1,0],[0,-1],[-1,0]]

        def mark(x,y):
            if x<0 or x>=rows or y<0 or y>=cols or board[x][y]!='O':
                return
            board[x][y]='T'
            for dr,dc in dirn:
                mark(x+dr,y+dc)          



        rows=len(board)
        cols=len(board[0])
        for i in range(rows):
            for j in range(cols):
                if i==rows-1 or j==cols-1 or i==0 or j==0:
                    if board[i][j]=='O':
                        mark(i,j)
                    
        for i in range(rows):
            for j in range(cols):
                if board[i][j]!='T':
                    board[i][j]='X'
                elif board[i][j]=='T':
                    board[i][j]='O'

        

                        

        
