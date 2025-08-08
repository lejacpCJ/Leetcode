from typing import List
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0  
        left = 0        
        fruit_count = defaultdict(int)  
        
        # Iterate through all trees with right pointer
        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1

            # Shrink window from left while we have more than 2 fruit types
            while len(fruit_count) > 2:
                # Remove leftmost fruit
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits