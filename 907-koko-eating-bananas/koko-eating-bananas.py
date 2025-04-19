class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minspeed=float('inf')
        left=1
        right=max(piles)
        while(left<=right):
            k=mid=(left+right)//2
            hrcount=0
            for i in piles:
                hrcount+=math.ceil(i/k)

            if hrcount<=h:
                minspeed=min(minspeed,k)
                right=k-1
            else:
                left=k+1

        return minspeed
