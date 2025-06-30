class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        minspeed=float('inf')
        while low<=high:
            k=(low+high)//2
            time=0
            for i in piles:
                time+=ceil(i/k)

            if time<=h:
                minspeed=min(minspeed,k)
                high=k-1
            else:
                low=k+1

        return minspeed