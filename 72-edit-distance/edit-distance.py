class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1 for _ in range(m+1)]for _ in range(n+1)]

        def f(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1

            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j]=0+f(i-1,j-1)
            else:
                dp[i][j]=min( 1+f(i,j-1) , 1+f(i-1,j), 1+f(i-1,j-1) ) #insert, delete, replace

            return dp[i][j]

        return f(n-1,m-1)
