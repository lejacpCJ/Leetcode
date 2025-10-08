from typing import List
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        for spell in spells:
            min_needed = (success + spell - 1) // spell  # Ceiling division
            idx = bisect_left(potions, min_needed)
            res.append(m - idx)

        return res