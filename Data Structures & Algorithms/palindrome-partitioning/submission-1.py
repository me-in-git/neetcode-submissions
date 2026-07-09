class Solution:
    def partition(self, s: str) -> List[List[str]]:
        h={} # stores whether a substring is a palindrome or not
        res=[]

        def ispal(s):
            if s in h:
                return h[s]
            if len(s)==1:
                return True
            
            for i in range(len(s)//2):
                if s[i]!=s[len(s)-i-1]:
                    h[s]=False
                    return False

            h[s]=True
            return True


        res=[]
        n=len(s)

        # def gensub(arr,ind):
        #     if ind==n:
        #         res.append(arr[:])
        #         return
            
        #     arr.append(ind)
        #     gensub(arr,ind+1)
        #     arr.pop()
        #     gensub(arr,ind+1)
        
        # gensub([],1)

        # fin = []
        # for cuts in res:
        #     if not cuts:
        #         if ispal(s):
        #             fin.append([s])
        #         else:
        #             continue  

        #     else:
        #         partition = []
        #         if ispal(s[0:cuts[0]]):
        #             partition.append(s[0:cuts[0]])
        #         else:
        #             continue

        #         for i in range(1, len(cuts)):
        #             if ispal(s[cuts[i-1]:cuts[i]]):
        #                 partition.append(s[cuts[i-1]:cuts[i]])
        #             else:
        #                 continue
                
        #         if ispal(s[cuts[-1]:len(s)]):
        #             partition.append(s[cuts[-1]:len(s)])
        #         else:
        #             continue
        #         fin.append(partition)


        def backtrack(start, path):
            if start == n:
                res.append(path[:])
                return

            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if ispal(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res





        