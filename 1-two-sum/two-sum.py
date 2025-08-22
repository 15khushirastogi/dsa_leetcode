class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[target-nums[i]]=i
            else:
                ind_val=d[nums[i]]
                return [ind_val,i]