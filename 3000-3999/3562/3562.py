from typing import List
from collections import defaultdict
from functools import lru_cache
import math

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        tree = defaultdict(list)
        for u, v in hierarchy:
            tree[u - 1].append(v - 1)

        @lru_cache(None)
        def dp(u):
            # Returns (dp0, dp1) for node u
            child_dp = [dp(v) for v in tree[u]]
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)
            for parent_bought, max_profits in [(0, dp0), (1, dp1)]:
                cost = present[u] if parent_bought == 0 else present[u] // 2
                profit = future[u] - cost

                dpA = [0] + [-math.inf] * budget
                dpB = [-math.inf] * (budget + 1)
                if cost <= budget:
                    dpB[cost] = profit
                for case0, case1 in child_dp:
                    new_dpA = [-math.inf] * (budget + 1)
                    for bgt in range(budget + 1):
                        if dpA[bgt] == -math.inf:
                            continue
                        for k in range(budget - bgt + 1):
                            if case0[k] == -math.inf:
                                continue
                            new_dpA[bgt + k] = max(new_dpA[bgt + k], dpA[bgt] + case0[k])
                    dpA = new_dpA

                    new_dpB = [-math.inf] * (budget + 1)
                    for bgt in range(budget + 1):
                        if dpB[bgt] == -math.inf:
                            continue
                        for k in range(budget - bgt + 1):
                            if case1[k] == -math.inf:
                                continue
                            new_dpB[bgt + k] = max(new_dpB[bgt + k], dpB[bgt] + case1[k])
                    dpB = new_dpB
                for bgt in range(budget + 1):
                    max_profits[bgt] = max(dpA[bgt], dpB[bgt])
            return dp0, dp1

        max_profits, _ = dp(0)
        return max(max_profits)