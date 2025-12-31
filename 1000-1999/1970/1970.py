from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        start = [(1, c) for c in range(1, col + 1)]

        def canCross(day):
            visited = set()
            for i in range(day):
                r, c = cells[i]
                visited.add((r, c))

            q = deque(start)
            while q:
                r, c = q.popleft()
                if not (0 < r <= row and 0 < c <= col) or (r, c) in visited:
                    continue
                if r == row:
                    return True
                visited.add((r, c))
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    q.append((nr, nc))
            return False

        left, right = 0, len(cells)

        while left < right:
            mid = (left + right + 1) // 2
            if not canCross(mid):
                right = mid - 1
            else:
                left = mid
        return left