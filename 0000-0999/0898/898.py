from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        curr = set()
        
        for num in arr:
            # Create new set for current position
            curr = {num | x for x in curr}
            # Add num to the set of current position
            curr.add(num)
            # Add all current OR values to result
            result |= curr
        
        return len(result)