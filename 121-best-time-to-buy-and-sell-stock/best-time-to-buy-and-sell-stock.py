class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxprofit=0
        bestbuy=prices[0]
        for i in range(1,n):
            if prices[i]>bestbuy:
                maxprofit=max(maxprofit,prices[i]-bestbuy)

            bestbuy=min(bestbuy,prices[i])

        return maxprofit