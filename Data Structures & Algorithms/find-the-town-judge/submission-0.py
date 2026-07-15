class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        poss=[[1,0] for i in range(n+1)]

        for a,b in trust:
            poss[a][0]=0
            poss[b][1]+=1

        ps=[]

        for i in range(1,n+1):
            a , b = poss[i][0],poss[i][1]
            if a==1 and b==n-1:
                ps.append(i)
            
        if len(ps)==1:
            return ps[0]
        
        return -1


