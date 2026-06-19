class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        stack=[0]
        for t in range(1,len(temp)):
            while stack and temp[t]>temp[stack[-1]]:
                el=stack.pop()
                res[el]=t-el
            stack.append(t)

        return res        



        