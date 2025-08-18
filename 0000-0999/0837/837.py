def new21Game(n: int, k: int, maxPts: int) -> float:
    # If Alice never draws or can never exceed n, she always wins
    if k == 0 or n >= k + maxPts:
        return 1.0

    # dp[x]: probability of starting from x points and final score be <= n
    dp = [0.0] * (n + maxPts + 1)
    # If Alice stops with x in [k, n], she wins
    for x in range(k, n + 1):
        dp[x] = 1.0

    # Initialize windowSum as the sum of dp[k..n]
    windowSum = n - k + 1  # sum of dp[k..n]
    for x in range(k - 1, -1, -1):
        dp[x] = windowSum / maxPts
        # Update windowSum for the next iteration
        windowSum += dp[x] - dp[x + maxPts]

    return dp[0]