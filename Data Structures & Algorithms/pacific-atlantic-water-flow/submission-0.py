class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        
        dirn=[[0,1],[1,0],[0,-1],[-1,0]]
        rows=len(h)
        cols=len(h[0])

        pac=[]
        atl=[]
        res=[]

        for i in range(rows):
            for j in range(cols):
                if j==0 or i==0:
                    pac.append([i,j])

                if i==rows-1 or j==cols-1:
                    atl.append([i,j])
                          
        def allpo(ocean):
            fin=[]
            q=deque(ocean)
            visited=set()
            for n in ocean:
                visited.add(tuple(n))

            while q:

                l=len(q)

                for _ in range(l):

                    a,b= q.popleft()
                    fin.append([a,b])

                    for dr,dc in dirn:
                        x=a+dr
                        y=b+dc
                        
                        if 0<=x<rows and 0<=y<cols and h[x][y]>=h[a][b] and (x,y) not in visited:
                            q.append([x,y])
                            visited.add((x,y))
            
            return fin

        pac_reach = allpo(pac)
        atl_reach = allpo(atl)
        pac_set = {tuple(cell) for cell in pac_reach}
        atl_set = {tuple(cell) for cell in atl_reach}
        return [list(cell) for cell in (pac_set & atl_set)]

                            
                        



           

            



        