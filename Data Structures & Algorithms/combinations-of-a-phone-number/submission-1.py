class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
        '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
        '8':['t','u','v'],'9':['w','x','y','z']}

        result=[]
        if not digits:
            return []

        def bt(arr,ind):
            
            if len(arr)==len(digits):
                result.append("".join(arr))
                return
            
            for ch in dic[digits[ind]]:
                arr.append(ch)
                bt(arr,ind+1)
                arr.pop()

        bt([],0) 
        return result           
            


        