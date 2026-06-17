class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap={}
        maxi=0
        l=0
        r=0
        while l<=r and r<len(s):
            while s[r] in hashmap:
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l+=1     
                          
            hashmap[s[r]]=hashmap.get(s[r],0)+1
            maxi=max(r-l+1,maxi)
            r+=1

        return maxi

            

