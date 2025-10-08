class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        
        for i in range(len(nums)):
            if nums[i]!=maxi and nums[i]!=mini:
                return nums[i]

        return -1