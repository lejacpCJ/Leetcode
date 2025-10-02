class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numEmpty = 0
        res = 0
        while numBottles > 0:
            res += numBottles
            numEmpty += numBottles
            numBottles = 0
            while numEmpty >= numExchange:
                numBottles += 1
                numEmpty -= numExchange
                numExchange += 1
        return res