class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        dirn=[[0,1],[1,0],[-1,0],[0,-1]]
        rows=len(board)
        cols=len(board[0])


        def search(x,y,ind):
            if ind==len(word):
                return True

            if x<0 or x>(rows-1) or y<0 or y>(cols-1) or ind>=len(word) or board[x][y]!=word[ind]:
                return False  

            temp=board[x][y]
            board[x][y]='*'            

            for dr,dc in dirn:
                nr,nc=x+dr,y+dc
                if search(nr,nc,ind+1):
                    return True
            
            board[x][y]=temp          


            


        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if search(i,j,0):
                        return True
        
        return False

        
            

            
