class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        suffix_zero = 0
        res = 0
        for i in range(n - 1, -1, -1):
            if i == n - 1 and s[i] == "0":
                suffix_zero += 1
            elif s[i] == "0":
                if s[i+1] != "0":
                    suffix_zero += 1
            else:
                res += suffix_zero
        return res