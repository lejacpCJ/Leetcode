from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        f = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(nums1, 1):
            for j, y in enumerate(nums2, 1):
                v = x * y
                f[i][j] = max(
                    f[i - 1][j],           # skip nums1[i-1]
                    f[i][j - 1],           # skip nums2[j-1]
                    max(0, f[i - 1][j - 1]) + v  # take both, or start new
                )
        return f[m][n]