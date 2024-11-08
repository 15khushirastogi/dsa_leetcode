class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        cumulative_xor = 0
        limit = (1 << maximumBit) - 1  

        for num in nums:
            cumulative_xor ^= num

        for num in reversed(nums):
            ans.append(cumulative_xor ^ limit)
            cumulative_xor ^= num  

        return ans
