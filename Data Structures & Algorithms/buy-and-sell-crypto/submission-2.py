class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        n = len(prices)

        max_profit = 0

        while sell < n:
            if prices[buy] >= prices[sell]:
                buy = sell
            else:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            sell += 1

        return max_profit