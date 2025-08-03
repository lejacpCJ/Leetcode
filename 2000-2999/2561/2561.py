from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Count frequency of each fruit type in both baskets
        count = Counter(basket1 + basket2)
        count1, count2 = Counter(basket1), Counter(basket2)
        all_keys = set(count1.keys()).union(count2.keys())
        # Find excess fruits in each basket
        excess1, excess2 = [], []

        # Check if it's possible to make baskets equal
        for key in all_keys:
            if (count1[key] + count2[key]) % 2 == 1:
                return -1
            target = (count1[key] + count2[key]) // 2
            if count1[key] > target:
                excess1.extend([key] * (count1[key] - target))
            if count2[key] > target:
                excess2.extend([key] * (count2[key] - target))
        
        # Sort excess fruits for optimal pairing
        excess1.sort()
        excess2.sort(reverse=True)
        
        # Find minimum element for indirect swaps
        min_element = min(basket1 + basket2)
        
        total_cost = 0
        for i in range(len(excess1)):
            # Direct swap vs indirect swap (through min element)
            direct_cost = min(excess1[i], excess2[i])
            indirect_cost = 2 * min_element
            total_cost += min(direct_cost, indirect_cost)
        
        return total_cost