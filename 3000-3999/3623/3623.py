from typing import List
from collections import defaultdict

MOD = 10 ** 9 + 7

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        groups = defaultdict(int)
        for x, y in points:
            groups[y] += 1

        combs = []
        for v in groups.values():
            if v >= 2:
                combs.append(v * (v - 1) // 2)

        n = len(combs)
        ans = 0
        partial_sum = 0
        for i in range(n):
            ans = (ans + combs[i] * partial_sum) % MOD
            partial_sum += combs[i]

        return ans