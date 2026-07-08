class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        s=set()
        t=set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    s.add(i)
                    t.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in s:
                    matrix[i][j]=0
                if j in t:
                    matrix[i][j]=0
                    

        
        