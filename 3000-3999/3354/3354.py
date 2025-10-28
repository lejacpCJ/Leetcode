class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        res = 0
        for x in nums:
            if x == 0:
                diff = total - 2 * prefix
                if diff == 0:
                    res += 2
                elif abs(diff) == 1:
                    res += 1
            prefix += x
        return res