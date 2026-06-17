class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi=0
        l=0
        r=0
        lenw=0
        hashmap={}
        while r<len(s):
            hashmap[s[r]]=hashmap.get(s[r],0)+1
            while hashmap and sum(hashmap.values()) - max(hashmap.values()) > k:
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l+=1
                lenw-=1
            
            lenw+=1
            maxi=max(lenw,maxi)
            r+=1        
        return maxi



            
            

        