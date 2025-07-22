from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        num_index = {}
        max_score = 0
        curr_sum = 0
        start = 0

        for i, num in enumerate(nums):
            # If num is already in the window, move start pointer
            if num in num_index and num_index[num] >= start:
                while start <= num_index[num]:
                    curr_sum -= nums[start]
                    start += 1
            curr_sum += num
            num_index[num] = i
            max_score = max(max_score, curr_sum)
        return max_score