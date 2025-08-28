from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # Sort bottom-left diagonals (including main diagonal) in non-increasing order
        for diag in range(n):
            i, j = diag, 0
            diagonal = []
            while i < n and j < n:
                diagonal.append(grid[i][j])
                i += 1
                j += 1
            diagonal.sort(reverse=True)
            i, j = diag, 0
            for num in diagonal:
                grid[i][j] = num
                i += 1
                j += 1

        # Sort top-right diagonals in non-decreasing order
        for diag in range(1, n):
            i, j = 0, diag
            diagonal = []
            while i < n and j < n:
                diagonal.append(grid[i][j])
                i += 1
                j += 1
            diagonal.sort()
            i, j = 0, diag
            for num in diagonal:
                grid[i][j] = num
                i += 1
                j += 1

        return grid