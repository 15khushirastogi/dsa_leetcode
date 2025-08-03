class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        bestBuy=prices[0]
        n=len(prices)
        for i in range(1,n):
            if prices[i]>bestBuy:
                maxProfit=max(maxProfit,prices[i]-bestBuy)
            
            bestBuy=min(bestBuy,prices[i])

        return maxProfit