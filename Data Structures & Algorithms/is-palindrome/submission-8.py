class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        print(s)
        s = ''.join(filter(str.isalnum, s))
        print(s)

        for i in range(len(s)//2):
            if s[i]!=s[len(s)-i-1]:
                return False
        
        return True
        
    
