class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        for key in d:
            if d[key]==1:
                return key
                

