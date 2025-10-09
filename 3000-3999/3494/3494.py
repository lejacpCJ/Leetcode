from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        prev_end = [0] * n  # Finish times for each wizard after previous potion

        for m in mana:
            cost = [m * s for s in skill]
            desired_start = [0] * n
            desired_start[0] = prev_end[0]
            for i in range(1, n):
                desired_start[i] = desired_start[i-1] + cost[i-1]
            wait = max(prev - des for prev, des in zip(prev_end, desired_start))
            prev_end[0] = desired_start[0] + wait + cost[0]
            for i in range(1, n):
                prev_end[i] = prev_end[i-1] + cost[i]
        return prev_end[-1]