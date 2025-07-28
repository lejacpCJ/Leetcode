from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        max_length = 0

        for val in range(k):

            dp = [0] * k
            for num in nums:
                prev_mod = (k + val - (num % k)) % k
                dp[num % k] = max(dp[num % k], dp[prev_mod] + 1)
            max_length = max(max_length, max(dp))
            
        return max_length