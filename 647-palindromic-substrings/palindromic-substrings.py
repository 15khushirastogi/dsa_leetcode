class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        def ispalindrome(start,end):
            s1=s[start:end+1]
            if s1==s1[::-1]:
                return True
            return False

        for i in range(n):
            for j in range(i,n):
                if(ispalindrome(i,j)):
                    count+=1

        return count
        