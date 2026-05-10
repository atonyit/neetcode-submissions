class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        for i in range(len(prices)):
            for j in range (i+1, len(prices)):
                if prices[j] - prices[i] > ans:
                    ans = prices[j] - prices[i]

        return ans


        #O(n2) time, O(1) space