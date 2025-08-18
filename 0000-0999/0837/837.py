def new21Game(n: int, k: int, maxPts: int) -> float:
    if k == 0 or n >= k + maxPts:
        return 1.0

    dp = [0.0] * (n + maxPts + 1)
    for x in range(k, n + 1):
        dp[x] = 1.0

    windowSum = n - k + 1  # sum of dp[k..n]
    for x in range(k - 1, -1, -1):
        dp[x] = windowSum / maxPts
        windowSum += dp[x] - dp[x + maxPts]

    return dp[0]