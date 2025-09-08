from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        digits = [int(c) for c in str(n)]
        other = [0] * len(digits)
        carry = False

        for i in range(len(digits) - 1, -1, -1):
            d = digits[i]
            if carry:
                if d > 2:
                    digits[i] -= 2
                    other[i] = 1
                    carry = False
                elif i:
                    if d == 2:
                        digits[i], other[i] = 9, 2
                    elif d == 1:
                        digits[i], other[i] = 9, 1
                    else:  # d == 0
                        digits[i], other[i] = 8, 1
                else:
                    other = other[1:]
                    if d == 2:
                        digits[i] = 1
                    elif d == 1:
                        digits = digits[1:]
            else:
                if d > 1:
                    digits[i] -= 1
                    other[i] = 1
                elif i:
                    carry = True
                    if d == 1:
                        digits[i], other[i] = 9, 2
                    else:  # d == 0
                        digits[i], other[i] = 9, 1
                else:
                    other = other[1:]
        return [int(''.join(str(x) for x in digits)), int(''.join(str(x) for x in other))]