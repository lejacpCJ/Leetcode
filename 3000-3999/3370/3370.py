class Solution:
    def smallestNumber(self, n: int) -> int:
        bit_len = len(bin(n)) - 2
        return 2 ** bit_len - 1