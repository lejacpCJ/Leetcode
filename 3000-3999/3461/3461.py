import math

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return True

        # weights correspond to binomial coefficients C(n-2, i) for i in [0..n-2]
        weights = [math.comb(n - 2, i) for i in range(n - 1)]

        left_weighted_sum = sum(int(s[i]) * weights[i] for i in range(n - 1))
        right_weighted_sum = sum(int(s[i + 1]) * weights[i] for i in range(n - 1))

        return left_weighted_sum % 10 == right_weighted_sum % 10