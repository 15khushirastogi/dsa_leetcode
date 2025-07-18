class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low=1
        high=num
        while(low<=high):
            mid=(low+high)//2
            if mid*mid==num:
                return True
            if mid*mid<num:
                low=mid+1
            else:
                high=mid-1

        return False