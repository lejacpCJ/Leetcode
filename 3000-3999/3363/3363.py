from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        dir2 = [(1, -1), (1, 0), (1, 1)]
        dir3 = [(-1, 1), (0, 1), (1, 1)]

        # Player 1: diagonal path from (0,0) to (n-1,n-1)
        player1 = sum(fruits[i][i] for i in range(n))

        # Player 2: from (0, n-1) to (n-1, n-1), staying in upper triangle
        player2 = [[-1] * n for _ in range(n)]
        player2[0][n - 1] = fruits[0][n - 1]
        for i in range(n):
            for j in range(i + 1, n):
                if player2[i][j] == -1:
                    continue
                for dr, dc in dir2:
                    x, y = i + dr, j + dc
                    if 0 <= x < n and 0 <= y < n and y > x:
                        player2[x][y] = max(player2[x][y], player2[i][j] + fruits[x][y])

        # Handle final position for player 2
        player2[n - 1][n - 1] = max(player2[n - 2][n - 1], player2[n - 2][n - 2])

        # Player 3: from (n-1, 0) to (n-1, n-1), staying in lower triangle
        player3 = [[-1] * n for _ in range(n)]
        player3[n - 1][0] = fruits[n - 1][0]
        for j in range(n):
            for i in range(j + 1, n):
                if player3[i][j] == -1:
                    continue
                for dr, dc in dir3:
                    x, y = i + dr, j + dc
                    if 0 <= x < n and 0 <= y < n and x > y:
                        player3[x][y] = max(player3[x][y], player3[i][j] + fruits[x][y])

        # Handle final position for player 3
        player3[n - 1][n - 1] = max(player3[n - 1][n - 2], player3[n - 2][n - 2])

        return player1 + player2[n - 1][n - 1] + player3[n - 1][n - 1]