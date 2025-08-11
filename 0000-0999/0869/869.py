class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Generate all powers of 2 from 2^0 to 2^30 (since 2^30 < 10^9 < 2^31)
        # Sort the digits of each power of 2 and store in a set for O(1) lookup
        power_sorted = set(''.join(sorted(str(1 << i))) for i in range(31))
        
        # Sort the digits of the input number to get canonical representation
        n_sorted = ''.join(sorted(str(n)))
        
        # Check if the sorted digits of n match any sorted digits of powers of 2
        return n_sorted in power_sorted