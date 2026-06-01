class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strarr1=[0]*26
        strarr2=[0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            strarr1[ord(s[i])-97]+=1
            strarr2[ord(t[i])-97]+=1
        
        if strarr1==strarr2:
            return True
        else:
            return False

            