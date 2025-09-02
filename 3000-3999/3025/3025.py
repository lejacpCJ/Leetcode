from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort points by x ascending, y descending
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        for i in range(len(points) - 1):
            max_height = points[i][1]  # y of the left point
            valid_height = -float('inf')  # Track the lowest y that blocks further pairs
            for j in range(i+1, len(points)):
                # Skip if right point is above left point
                if points[j][1] > max_height:
                    continue
                # If right point is on the same horizontal line, count and break (no more valid below)
                if points[j][1] == max_height:
                    res += 1
                    break
                # Skip if blocked by a previous point
                if points[j][1] <= valid_height:
                    continue
                # Update the lowest blocking y and count this pair
                valid_height = max(valid_height, points[j][1])
                res += 1
        return res