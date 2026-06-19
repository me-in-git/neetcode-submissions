class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        heap=[]
        print(freq)
        for num,count in freq.items():
            heap.append([-count,num])
        heapq.heapify(heap)
        res=[]
        while k:
            res.append(heap[0][1])
            heapq.heappop(heap)
            k-=1

        return res
        