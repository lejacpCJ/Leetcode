from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n, x, y = len(mat), len(mat[0]), 0, 0
        lst = []
        curr_dir = "up_right"

        while len(lst) < m * n:
            lst.append(mat[y][x])
            if curr_dir == "up_right":
                x += 1
                y -= 1
                if x >= n:
                    x -= 1
                    y += 2
                    curr_dir = "down_left"
                elif y < 0:
                    y += 1
                    curr_dir = "down_left"
            elif curr_dir == "down_left":
                x -= 1
                y += 1
                if y >= m:
                    y -= 1
                    x += 2
                    curr_dir = "up_right"
                elif x < 0:
                    x += 1
                    curr_dir = "up_right"
        return lst