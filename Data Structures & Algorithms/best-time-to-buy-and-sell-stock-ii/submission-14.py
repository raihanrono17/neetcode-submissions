class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] <= prices[i-1]:
                p = prices[i-1] - buy
                profit = profit + p
                buy = prices[i]
            elif i == len(prices) -1 and prices[i-1] == buy:
                p = prices[i] - buy
                profit += p
            elif buy == prices[0] and i == len(prices) -1:
                profit = prices[i] - buy 
            elif buy < prices[i] and i == len(prices) -1:
                p = prices[i] - buy
                profit = profit + p
        return profit
