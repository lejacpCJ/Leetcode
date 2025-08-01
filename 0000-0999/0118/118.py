from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize result with the first row of Pascal's triangle
        res = [[1]]
        
        # Generate each row from 1 to numRows-1
        for i in range(1, numRows):
            # Create a new empty row
            res.append([])
            
            # Start each row with 1
            res[i].append(1)
            
            # Fill the middle elements of the row
            # Each element is the sum of two elements above it
            for j in range(i - 1):
                res[i].append(res[i - 1][j] + res[i - 1][j + 1])
            
            # End each row with 1
            res[i].append(1)
        
        return