from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            s = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if sorted(s) != list(range(1, 10)):
                return False
            return (s[0] + s[1] + s[2] == 15 and
                    s[3] + s[4] + s[5] == 15 and
                    s[6] + s[7] + s[8] == 15 and
                    s[0] + s[3] + s[6] == 15 and
                    s[1] + s[4] + s[7] == 15 and
                    s[2] + s[5] + s[8] == 15 and
                    s[0] + s[4] + s[8] == 15 and
                    s[2] + s[4] + s[6] == 15)

        m, n = len(grid), len(grid[0])
        res = 0
        if n < 3 or m < 3:
            return res
        for i in range(m - 2):
            for j in range(n - 2):
                if isMagic(i, j):
                    res += 1
        return res