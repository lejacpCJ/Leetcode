from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = 0
        
        # Process each fruit type from left to right
        for fruit in fruits:
            placed = False
            
            # Find the leftmost available basket with sufficient capacity
            for i, basket in enumerate(baskets):
                if basket != -1 and basket >= fruit:
                    baskets[i] = -1  # Mark basket as used
                    placed = True
                    break
            
            # If fruit couldn't be placed, increment result counter
            if not placed:
                result += 1
        
        return result