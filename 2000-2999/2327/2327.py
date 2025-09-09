MOD = 10**9 + 7

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for day in range(2, n + 1):
            for share_day in range(max(1, day - forget + 1), day - delay + 1):
                dp[day] = (dp[day] + dp[share_day]) % MOD

        # Sum people who still remember the secret at the end
        return sum(dp[max(1, n - forget + 1): n + 1]) % MOD