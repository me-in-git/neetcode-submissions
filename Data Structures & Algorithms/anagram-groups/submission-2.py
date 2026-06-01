class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getlist(string):
            lis=[0]*26
            for ch in string:
                lis[ord(ch)-97]+=1
            return tuple(lis)

        
        hashmap=defaultdict(list)
        for word in strs:
            hashmap[getlist(word)].append(word)

        return list(hashmap.values())
        



