from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # The maximum possible AND is the maximum element in the array
        max_val = max(nums)
        
        result = 0
        curr = 0
        
        # Find the longest consecutive sequence of max_val
        for num in nums:
            if num == max_val:
                curr += 1
                result = max(result, curr)
            else:
                curr = 0
        
        return result