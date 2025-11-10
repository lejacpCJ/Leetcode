class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        q = []
        for num in nums:
            while q and q[-1] > num:
                q.pop()
            if num == 0:
                continue
            if not q or q[-1] < num:
                count += 1
                q.append(num)
        return count