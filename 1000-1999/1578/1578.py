class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        n = len(colors)
        curr = ""
        curr_time = 0
        curr_max = 0
        i = 0
        while i < n:
            if colors[i] != curr:
                if curr_time > curr_max:
                    res += curr_time - curr_max
                curr = colors[i]
                curr_time = neededTime[i]
                curr_max = neededTime[i]
            else:
                curr_time += neededTime[i]
                curr_max = max(curr_max, neededTime[i])
            i += 1

        if curr_time > curr_max:
            res += curr_time - curr_max

        return res