class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i=1
        n=len(nums)
        freq=1
        while(i<n):
            if nums[i]==nums[i-1]:
                freq+=1
            else:
                freq=1
            
            if freq>(n//2):
                return nums[i]
            i+=1
        return nums[0]
    