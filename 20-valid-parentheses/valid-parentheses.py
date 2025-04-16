class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','{':'}','[':']'}
        stack=[]
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i)
            else:
                if not stack or d[stack[-1]] != i:
                    return False
                
                stack.pop()

        return not stack