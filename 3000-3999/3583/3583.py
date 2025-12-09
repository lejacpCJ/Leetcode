from collections import Counter

MOD = 10**9 + 7

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = Counter(nums)
        prefix = Counter()
        result = 0

        for j in range(n):
            suffix[nums[j]] -= 1
            target = nums[j] * 2
            count_i = prefix[target]
            count_k = suffix[target]
            result = (result + count_i * count_k) % MOD
            prefix[nums[j]] += 1

        return result