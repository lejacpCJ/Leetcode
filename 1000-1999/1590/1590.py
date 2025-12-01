class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        curr = 0
        ans = len(nums)
        seen = {0: -1}
        for i, x in enumerate(nums):
            curr = (curr + x) % p
            need = (curr - target) % p
            if need in seen:
                ans = min(ans, i - seen[need])
            seen[curr] = i
        return -1 if ans == len(nums) else ans