class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_d=sorted(d.items(), key=lambda item:item[1], reverse=True)
        

        for i in range(k):
            ans.append(sorted_d[i][0])

        return ans

        