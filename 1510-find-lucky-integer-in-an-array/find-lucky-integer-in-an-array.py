class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        ans=-1
        for key,value in d.items():
            if key==value:
                ans=max(ans,key)

        return ans