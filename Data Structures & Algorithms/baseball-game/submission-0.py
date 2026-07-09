class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s=[]
        for i in range(len(ops)):
            if ops[i]=='C':
                s.pop()
            elif ops[i]=='D':
                s.append(s[-1]*2)
            elif ops[i]=='+':

                s.append(s[-1]+s[-2])
            else:
                s.append(int(ops[i]))
            
        return sum(s)

        