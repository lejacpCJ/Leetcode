from typing import List
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_dict = defaultdict(list)
        y_dict = defaultdict(list)
        buildings.sort()
        for x, y in buildings:
            x_dict[x].append(y)
            y_dict[y].append(x)
        ans = 0
        for x, y in buildings:
            x_covered = x > y_dict[y][0] and x < y_dict[y][-1]
            y_covered = y > x_dict[x][0] and y < x_dict[x][-1]
            if x_covered and y_covered:
                ans += 1
        return ans