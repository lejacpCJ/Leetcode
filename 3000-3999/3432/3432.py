from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        sum_nums = sum(nums)
        pre_sum = 0
        for i in range(len(nums) - 1):
            pre_sum += nums[i]
            diff = sum_nums - pre_sum * 2
            if diff % 2 == 0:
                ans += 1
        return ans