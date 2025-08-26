from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        res = 0
        for length, width in dimensions:
            curr_diag = length ** 2 + width ** 2
            area = length * width
            if curr_diag > max_diag:
                max_diag = curr_diag
                res = area
            elif curr_diag == max_diag:
                res = max(res, area)
        return res