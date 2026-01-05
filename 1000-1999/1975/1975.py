from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_abs = float('inf')
        neg_count = 0
        total = 0
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                abs_val = abs(val)
                min_abs = min(min_abs, abs_val)
                if val < 0:
                    neg_count += 1
                total += abs_val
        if neg_count % 2 == 0:
            return total
        return total - 2 * min_abs