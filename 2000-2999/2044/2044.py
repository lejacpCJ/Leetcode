from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        def backtrack(index: int, current_or: int) -> int:
            if index == len(nums):
                return 1 if current_or == max_or else 0
            
            # Skip current element
            count = backtrack(index + 1, current_or)
            
            # Include current element
            count += backtrack(index + 1, current_or | nums[index])
            
            return count
        
        return backtrack(0, 0)