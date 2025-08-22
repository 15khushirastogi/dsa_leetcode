class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        s=set()
        for i in nums:
            s.add(i)
        longest=1

        for i in s:
            if i-1 not in s:
                cnt=1
                x=i
                while x+1 in s:
                    x+=1
                    cnt+=1
                longest=max(longest,cnt)

        return longest