from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        for i in range(len(points) - 1):
            max_height = points[i][1]
            valid_height = -float('inf')
            for j in range(i+1, len(points)):
                if points[j][1] > max_height:
                    continue
                if points[j][1] == max_height:
                    res += 1
                    break
                if points[j][1] <= valid_height:
                    continue
                valid_height = max(valid_height, points[j][1])
                res += 1
        return res