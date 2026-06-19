class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]        
        heapq.heapify(heap)        

        while len(heap)>1:
            if heap[0]==heap[1]:
                heapq.heappop(heap)
                heapq.heappop(heap)
            else:
                p=heapq.heappop(heap)
                q=heapq.heappop(heap)
                heapq.heappush(heap,p-q)

        return -heap[0] if heap else 0



