from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Helper to calculate the gain of adding a student
        def gain(p, t):
            return (p + 1) / (t + 1) - (p / t)
        
        # Max heap: store (-gain, p, t)
        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p, t), p, t))
        
        for _ in range(extraStudents):
            neg_delta, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))
        
        total = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t
        
        return total / len(classes)