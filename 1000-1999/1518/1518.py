class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numEmpty = 0
        res = 0
        while numBottles > 0 or numEmpty >= numExchange:
            res += numBottles
            numEmpty += numBottles
            numBottles, numEmpty = divmod(numEmpty, numExchange)
        return res