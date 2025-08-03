class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        for key in d:
            if d[key]>(n/2):
                return key