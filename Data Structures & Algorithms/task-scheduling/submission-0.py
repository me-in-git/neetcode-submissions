class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        
        freq = list(Counter(tasks).values())
        maxf = max(freq)
        count_max = freq.count(maxf)
        
        return max(len(tasks), (maxf - 1) * (n + 1) + count_max)
