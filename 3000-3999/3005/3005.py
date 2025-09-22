from typing import List
from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        max_freq = max(freqs.values())

        res = 0
        for num in nums:
            if freqs[num] == max_freq:
                res += 1

        return res