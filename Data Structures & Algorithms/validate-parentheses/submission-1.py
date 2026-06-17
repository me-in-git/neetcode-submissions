class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if not stack or ch == ')' and stack[-1]!='(' or ch == ']' and stack[-1]!='[' or ch == '}' and stack[-1]!='{':
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False

        