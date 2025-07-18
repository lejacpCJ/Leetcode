import heapq
from typing import List
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        left_sum = [0] * 3 * n
        right_sum = [0] * 3 * n
        
        heap = []
        curr_sum = 0

        for i in range(2 * n):
            heapq.heappush(heap, -nums[i])
            curr_sum += nums[i]

            if len(heap) > n:
                curr_sum -= -heapq.heappop(heap)
            if len(heap) == n:
                left_sum[i] = curr_sum
            else:
                left_sum[i] = float('inf')


        heap = []
        curr_sum = 0
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(heap, nums[i])
            curr_sum += nums[i]

            if len(heap) > n:
                curr_sum -= heapq.heappop(heap)
            if len(heap) == n:
                right_sum[i] = curr_sum
            else:
                right_sum[i] = float('-inf')
        
        res = float('inf')

        for i in range(n -1 , 2 * n):
            res = min(res, left_sum[i] - right_sum[i+1])
        return res
        
