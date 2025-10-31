class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_set = set()
        res = []
        for num in nums:
            if num in num_set:
                res.append(num)
            else:
                num_set.add(num)
        return res