class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashs1=Counter(s1)
        l=0
        r=0
        hashs2={}
        lenw=0
        while r<len(s2):
            hashs2[s2[r]]=hashs2.get(s2[r],0)+1
            lenw+=1
            if lenw>len(s1):
                hashs2[s2[l]]-=1
                if hashs2[s2[l]]==0:
                    del hashs2[s2[l]]
                lenw-=1
                l+=1
            if lenw==len(s1):
                if hashs1==hashs2:
                    return True
            r+=1
        return False





        