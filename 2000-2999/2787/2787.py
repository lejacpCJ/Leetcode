class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        # Find maximum base whose x-th power <= n
        epsilon = 1e-9
        max_n = int(n ** (1/x) + epsilon)

        # Generate all x-th powers: 1^x, 2^x, ..., max_n^x
        nums = [val ** x for val in range(1, max_n + 1)]

        # dp[i] = number of ways to express i as sum of unique x-th powers
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one way to make 0

        # For each power, update dp array (iterate backwards to avoid reuse)
        for num in nums:
            for target in range(n, num - 1, -1):
                dp[target] = (dp[target] + dp[target - num]) % MOD

        return dp[n]