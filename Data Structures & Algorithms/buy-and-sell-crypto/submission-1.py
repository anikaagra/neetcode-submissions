class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        n = len(prices)

        max_profit = 0

        while buy < sell and buy < n - 1 and sell < n:
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            elif prices[buy] <= prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
                sell += 1

        return max_profit