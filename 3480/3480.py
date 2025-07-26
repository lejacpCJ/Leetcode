from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # Group pairs by their right endpoints
        right = [[] for _ in range(n+1)]
        
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
        res = 0                    # Total valid subarrays keeping all pairs
        max_lefts = [0, 0]        # Track two largest left endpoints
        gain = defaultdict(int)   # Potential gain from removing each left endpoint
        
        # Sweep from left to right
        for i in range(1, n+1):
            # Process all pairs ending at position i
            for l in right[i]:
                max_lefts.append(l)
                max_lefts.sort()     # Keep only largest 2 (max 3 elements total)
                max_lefts.pop(0)     # Remove smallest
            
            # Count valid subarrays ending at position i
            # Can start from any position > max_lefts[1] (second largest left)
            res += (i - max_lefts[1])
            
            # Calculate gain from removing the pair with left endpoint max_lefts[1]
            # This frees up subarrays blocked only by this pair
            gain[max_lefts[1]] += (max_lefts[1] - max_lefts[0])
        
        # Return total valid subarrays plus maximum possible gain
        return res + max(gain.values())