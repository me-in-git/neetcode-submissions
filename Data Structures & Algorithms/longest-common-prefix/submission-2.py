class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ind=0
        res=[]
        smallest = min(strs, key=len)

        while ind<len(smallest):
            ch=strs[0][ind]
            for i in range(len(strs)):
                if strs[i][ind]!=ch:
                    return ''.join(res)

            res.append(ch)
            ind+=1
        return ''.join(res)     


                   