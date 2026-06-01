from typing import List
import math
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos=[]
        neg=[]
        zero=[]
        for i in nums:
            if i<0:
                neg.append(i)
            elif i==0:
                zero.append(i)
            else:
                pos.append(i)

        res=[]
        def twosum(target,arr,og):
            hashmap={}
            output=[]
            arr= arr+zero
            for i in range(len(arr)):
                complement=target-arr[i]
                if complement in hashmap:
                    output.append([og,arr[i],complement])
                hashmap[arr[i]]=1
            return output

        for i in neg:
            res+=(twosum(-1*i,pos,i))
        for i in pos:
            res+=(twosum(-1 *i,neg,i))
        if len(zero) >= 3:
            res.append([0,0,0])
        
        unique = set(tuple(sorted(triplet)) for triplet in res)
        return [list(triplet) for triplet in unique]
