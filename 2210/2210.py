from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums_set = [nums[0]]
        
        # Remove consecutive duplicates
        for i in range(1, len(nums)):
            if nums[i] == nums_set[-1]:
                continue
            nums_set.append(nums[i])
        
        # Count hills and valleys
        res = 0
        for i in range(1, len(nums_set) - 1):
            if ((nums_set[i-1] > nums_set[i] and nums_set[i+1] > nums_set[i]) or
                (nums_set[i-1] < nums_set[i] and nums_set[i+1] < nums_set[i])):
                res += 1
        
        return res