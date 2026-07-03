class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def bt(arr,total):
            if total>n or total<0:
                return 
            if len(arr)==2*n:
                if total==0:
                    result.append("".join(arr))
                return
           
            
            arr.append('(')
            bt(arr,total+1)
            arr.pop()
            arr.append(')')
            bt(arr,total-1)
            arr.pop()
        
        bt([],0)
        return result

            
