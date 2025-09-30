from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        coef = 1
        for i in range(1, n+1):
            res += nums[i-1] * coef
            res %= 10
            coef = coef * (n - i) // i
        return res