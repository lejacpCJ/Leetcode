from typing import List

class Solution:
    def maxPointsOnALine(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0  # Maximum fruits we can collect
        left = 0        # Left pointer for sliding window
        current_sum = 0 # Current sum of fruits in the window
        
        # Iterate through all fruit positions with right pointer
        for right, (right_pos, right_amount) in enumerate(fruits):
            # Add current fruit to our collection
            current_sum += right_amount
            
            # Shrink window from left while range is not reachable within k steps
            while (
                left <= right and
                # Calculate minimum steps needed for current range [left, right]
                # Range distance + shorter distance from startPos to either end
                (right_pos - fruits[left][0] + 
                 min(abs(startPos - fruits[left][0]), abs(startPos - right_pos))) > k
            ):
                # Remove leftmost fruit and move left pointer
                current_sum -= fruits[left][1]
                left += 1
            
            # Update maximum fruits collected
            max_fruits = max(max_fruits, current_sum)
        
        return max_fruits