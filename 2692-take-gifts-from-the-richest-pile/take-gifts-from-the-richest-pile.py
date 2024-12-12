class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts.sort()
            gifts[-1]=int(pow(gifts[-1],0.5))

        return sum(gifts)