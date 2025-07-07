class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in arr:
            if i<=k:
                k+=1
            else:
                break

        return k

