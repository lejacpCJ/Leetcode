import bisect

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        candidates = list(nums)
        for num in nums:
            candidates.append(num + k)
            candidates.append(num - k)

        candidates = sorted(set(candidates))
        maps = {val: idx for idx, val in enumerate(candidates)}
        n = len(candidates)
        freq = [0] * n
        prefix_sum = [0] * (n + 1)
        for num in nums:
            freq[maps[num]] += 1

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + freq[i - 1]

        max_freq = 1

        for i in range(n):
            left = bisect.bisect_left(candidates, candidates[i] - k)
            right = bisect.bisect_right(candidates, candidates[i] + k)

            changeable = prefix_sum[right] - prefix_sum[left] - freq[i]
            max_freq = max(max_freq, min(changeable, numOperations) + freq[i])

        return max_freq