import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        gcd_all = 0
        ones = 0
        min_len = 10 ** 6

        for num in nums:
            gcd_all = math.gcd(gcd_all, num)
            if num == 1:
                ones += 1
        if gcd_all != 1:
            return -1
        if ones > 0:
            return len(nums) - ones

        for i in range(len(nums)):
            curr_gcd = nums[i]
            for j in range(i+1, len(nums)):
                curr_gcd = math.gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        return len(nums) + min_len - 2