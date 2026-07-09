class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sep(arr):
            if len(arr)<=1:
                return arr

            mid=len(arr)//2
            l=arr[:mid]
            r=arr[mid:]

            leftsorted=sep(l)
            rightsorted=sep(r)

            return merge(leftsorted,rightsorted)

        def merge(l,r):
            res=[]
            i=0
            j=0
            while i<len(l) and j<len(r):
                if l[i]<=r[j]:
                    res.append(l[i])
                    i+=1
                else:
                    res.append(r[j])
                    j+=1
            
            while i<len(l):
                res.append(l[i])
                i+=1
            
            while j<len(r):
                res.append(r[j])
                j+=1

            return res
        

        return sep(nums)


        