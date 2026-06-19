class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x,y in points:
            heap.append([abs(x)**2+abs(y)**2,x,y])
        
        heapq.heapify(heap)
        res=[]
        while k:
            res.append([heap[0][1],heap[0][2]])
            heapq.heappop(heap)
            k-=1
        return res
