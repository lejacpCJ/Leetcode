from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def trapezoid(n):
            return n * (n + 1) // 2
        
        res = 0
        curr = 0

        for num in nums:
            if num == 0:
                curr += 1
            else:
                res += trapezoid(curr)
                curr = 0
        res += trapezoid(curr)  # Add the last sequence if it ends with zeros

        return res