class Solution:
    def maxUniqueSubarraySum(self, nums: List[int]) -> int:
        res = 0
        history = set()
        hasAdded = False
        
        for num in nums:
            if num <= 0 or num in history:
                continue
            history.add(num)
            res += num
            hasAdded = True
        
        if not hasAdded:
            return max(nums)
        
        return res