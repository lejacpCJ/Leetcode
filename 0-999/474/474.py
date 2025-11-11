class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Preprocess: count zeros and ones for each string
        counts = [(s.count('0'), s.count('1')) for s in strs]

        for zero, one in counts:
            for i in range(n, one - 1, -1):
                for j in range(m, zero - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - one][j - zero] + 1)

        return max(max(row) for row in dp)