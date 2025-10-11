class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=float('-inf')
        prod=1
        for i in range(n):
            prod*=nums[i]
            maxi=max(maxi,prod)
            if prod==0:
                prod=1
        prod=1
        for i in range(n-1,-1,-1):
            prod*=nums[i]
            maxi=max(maxi,prod)
            if prod==0:
                prod=1

        return maxi