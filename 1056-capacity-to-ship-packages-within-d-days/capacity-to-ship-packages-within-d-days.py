class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2
            daycount = 1
            load = 0
            for weight in weights:
                if load + weight > mid:
                    daycount += 1
                    load = weight
                else:
                    load += weight

            if daycount > days:
                low = mid + 1
            else:
                ans = min(ans, mid) 
                high = mid - 1

        return ans
