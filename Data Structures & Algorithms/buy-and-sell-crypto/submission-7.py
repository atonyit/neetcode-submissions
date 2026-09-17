class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy, sell, best = 0, 1, 0

        while sell < len(prices):
            best = max(prices[sell] - prices[buy], best)
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1

        return best
            