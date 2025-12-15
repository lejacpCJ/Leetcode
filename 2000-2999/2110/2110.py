from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        straight = 1
        for i in range(n - 1):
            if prices[i] - prices[i + 1] == 1:
                straight += 1
            else:
                ans += (straight + 1) * straight // 2
                straight = 1
        ans += (straight + 1) * straight // 2
        return ans