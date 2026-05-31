class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=1
        profit=0
        for i in range (len(prices)):
            if r<len(prices) and prices[r]>prices[i]:
                profit+=prices[r]-prices[i]
            r+=1
        return profit
