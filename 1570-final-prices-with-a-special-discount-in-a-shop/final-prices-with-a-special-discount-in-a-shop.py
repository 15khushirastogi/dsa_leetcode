class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        res=prices[:]
        s=[]
        for i in range(n):
            while s and prices[s[-1]]>=prices[i]:
                pos=s.pop()
                res[pos]-=prices[i]
            s.append(i)
        return res