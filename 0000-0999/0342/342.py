# Check if n is positive, has only one '1' in binary, and even number of trailing zeros (power of four)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        binary_str = format(n, 'b')
        zero_count = 0

        for bit in binary_str[1:]:
            if bit == '1':
                return False
            zero_count += 1
        
        if zero_count % 2 == 0:
            return True
        return False