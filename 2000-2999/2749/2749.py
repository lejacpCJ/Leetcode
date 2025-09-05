import math

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            m = num1 - k * num2
            if m < k:
                break
            if bin(m).count("1") <= k:
                return k
        return -1