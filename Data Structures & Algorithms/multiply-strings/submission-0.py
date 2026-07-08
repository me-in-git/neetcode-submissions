class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic={'1':1 ,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}

        def makenum(s):
            m=1
            val=0
            for i in range(len(s)-1,-1,-1):
                val+=dic[s[i]]*m
                m*=10
            return val
        

        return str(makenum(num1)*makenum(num2))


        