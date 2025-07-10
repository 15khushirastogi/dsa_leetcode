class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        low = max(nums)
        high = sum(nums)
        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2
            arraycount = 1
            runningSum = 0
            maxSubarraySum = 0  

            for i in range(n):
                if runningSum + nums[i] <= mid:
                    runningSum += nums[i]
                else:
                    maxSubarraySum = max(maxSubarraySum, runningSum)
                    arraycount += 1
                    runningSum = nums[i]  

            maxSubarraySum = max(maxSubarraySum, runningSum) 

            if arraycount == k:
                ans = min(ans, maxSubarraySum)
                high = mid - 1
            elif arraycount > k:
                low = mid + 1
            else:
                ans = min(ans, maxSubarraySum)
                high = mid - 1

        return ans
