class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        # Compute prefix sum for fast range queries
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + stations[i - 1]

        # Calculate initial power for each city
        power = [0] * n
        for i in range(n):
            # Power is sum of stations in [i-r, i+r]
            power[i] = presum[min(i + r + 1, n)] - presum[max(i - r, 0)]

        # Binary search for the maximum possible minimum power
        left = min(power)
        right = left + k
        while left <= right:
            mid = left + (right - left) // 2
            # Check if it's possible to achieve at least 'mid' power everywhere
            if self.check(mid, power, n, r, k):
                left = mid + 1
            else:
                right = mid - 1
        return right

    def check(self, minPower: int, power: List[int], n: int, r: int, k: int) -> bool:
        # Difference array for efficient range updates
        diff = [0] * n
        need = 0
        sumD = 0
        for i in range(n):
            sumD += diff[i]
            # Calculate how many more stations are needed at city i
            m = minPower - power[i] - sumD
            if m > 0:
                need += m
                if need > k:
                    return False  # Not enough stations left to allocate
                sumD += m
                # Remove the effect of added stations after their range ends
                if i + 2 * r + 1 < n:
                    diff[i + 2 * r + 1] -= m
        return True