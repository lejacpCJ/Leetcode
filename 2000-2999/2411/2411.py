from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Store the rightmost position where each bit is set
        bit_positions = [0] * 32
        result = [0] * n
        
        # Process from right to left
        for i in range(n - 1, -1, -1):
            # Update bit positions for current number
            for bit in range(32):
                if nums[i] & (1 << bit):
                    bit_positions[bit] = i
            
            # Find the furthest bit position needed for maximum OR
            # This determines the minimum subarray length
            result[i] = max(1, max(bit_positions) - i + 1)

        return result