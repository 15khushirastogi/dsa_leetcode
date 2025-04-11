class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m=len(g)
        n=len(s)
        left=0
        right=0
        while(left<n and right<m):
            if(s[left]>=g[right]):
                left+=1
                right+=1
            else:
                left+=1

        return right
