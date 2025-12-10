class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(complexity)
        for i in range(1, n):
            if complexity[0] >= complexity[i]:
                return 0
        # Compute factorial (n-1)!
        fact = 1
        for i in range(1, n):
            fact = (fact * i) % MOD
        return fact