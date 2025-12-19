from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        m = k // 2

        # Compute prefix sums for efficient window calculations
        s1 = [0] * (n - m + 1)  # sum of strategy[i] * prices[i] for window of size m
        s2 = [0] * (n - m + 1)  # sum of prices[i] for window of size m

        s1[0] = sum(prices[i] * strategy[i] for i in range(m))
        s2[0] = sum(prices[i] for i in range(m))

        for i in range(n - m):
            s1[i + 1] = s1[i] - prices[i] * strategy[i] + prices[i + m] * strategy[i + m]
            s2[i + 1] = s2[i] - prices[i] + prices[i + m]

        total_profit = sum(prices[i] * strategy[i] for i in range(n))
        ans = total_profit

        for i in range(n - k + 1):
            # Remove the original profit in the window, add the profit after modification
            # First m elements set to 0, last m elements set to 1
            profit = total_profit - s1[i] - s1[i + m] + s2[i + m]
            ans = max(ans, profit)

        return ans