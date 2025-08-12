from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        
        # Find powers of 2 that sum to n by examining binary representation
        binary_str = format(n, 'b')
        powers = []
        
        # Extract exponents of powers of 2 from binary representation
        for i in range(len(binary_str) - 1, -1, -1):
            if binary_str[i] == '1':
                powers.append(len(binary_str) - i - 1)
        
        answers = []
        for q in queries:
            l, r = q[0], q[1]
            
            if l == r:
                # Single element query
                answers.append(2 ** powers[l] % MOD)
            else:
                # Range query: sum exponents and compute 2^sum
                exponent_sum = sum(powers[l:r+1])
                answers.append(2 ** exponent_sum % MOD)
        
        return answers