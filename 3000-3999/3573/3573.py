from typing import List
import math

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # DP arrays for current and previous day:
        # flat[t]  - no open position, t completed transactions
        # long[t]  - in a normal (long) transaction
        # short[t] - in a short transaction
        NEG_INF = -10**18

        prev_flat = [NEG_INF] * (k + 1)
        prev_long = [NEG_INF] * (k + 1)
        prev_short = [NEG_INF] * (k + 1)

        # Before day 0: flat with 0 completed transactions, profit = 0
        prev_flat[0] = 0

        for price in prices:
            cur_flat = [NEG_INF] * (k + 1)
            cur_long = [NEG_INF] * (k + 1)
            cur_short = [NEG_INF] * (k + 1)

            for t in range(k + 1):
                # 1) From flat[t]
                if prev_flat[t] != NEG_INF:
                    # Stay flat
                    cur_flat[t] = max(cur_flat[t], prev_flat[t])

                    if t < k:
                        # Start normal (buy today)
                        cur_long[t] = max(cur_long[t], prev_flat[t] - price)
                        # Start short (sell today)
                        cur_short[t] = max(cur_short[t], prev_flat[t] + price)

                # 2) From long[t] (normal running)
                if prev_long[t] != NEG_INF:
                    # Keep holding long
                    cur_long[t] = max(cur_long[t], prev_long[t])

                    # Close normal (sell today)
                    if t + 1 <= k:
                        cur_flat[t + 1] = max(cur_flat[t + 1], prev_long[t] + price)

                # 3) From short[t] (short running)
                if prev_short[t] != NEG_INF:
                    # Keep holding short
                    cur_short[t] = max(cur_short[t], prev_short[t])

                    # Close short (buy back today)
                    if t + 1 <= k:
                        cur_flat[t + 1] = max(cur_flat[t + 1], prev_short[t] - price)

            prev_flat, prev_long, prev_short = cur_flat, cur_long, cur_short

        # Best profit must be with no open position
        return max(prev_flat)