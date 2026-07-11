class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:      


        res=[]
        x=newInterval[0]
        y=newInterval[1]
        n = len(intervals)
        i=0

        while i < n and intervals[i][1]< x:
            res.append(intervals[i])
            i+=1
        

        while i<n and y >= intervals[i][0]:
            x= min(x,intervals[i][0])
            y = max(intervals[i][1],y)
            i+=1

        res.append([x,y])

        while i<n:
            res.append(intervals[i])
            i+=1
        
        return res

        




        
        