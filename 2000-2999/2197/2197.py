import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and math.gcd(stack[-1], num) > 1:
                num = math.lcm(stack.pop(), num)
            stack.append(num)
        return stack