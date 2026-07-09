class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=[]
        summ=0
        res=0
        hashmap={}
        for i,num in enumerate(nums):
            summ+=num
            prefix_sum.append(summ)
                    
            if prefix_sum[i]==k:
                res+=1
            tar= prefix_sum[i]-k
            if tar in hashmap:
                res+=hashmap[tar]
            hashmap[summ]=hashmap.get(summ,0)+1
            
        
        return res


        
