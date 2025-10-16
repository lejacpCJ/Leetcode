class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods = [0] * value
        for num in nums:
            mods[num % value] += 1
        min_mod = min(mods)
        min_i = mods.index(min_mod)
        return min_mod * value + min_i