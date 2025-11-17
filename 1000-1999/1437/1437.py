class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        curr_dist = -1
        for i in range(n):
            if nums[i] == 1:
                if curr_dist != -1 and curr_dist < k:
                    return False
                curr_dist = 0
            else:
                if curr_dist != -1:
                    curr_dist += 1
        return True