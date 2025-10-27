class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev_devices = 0
        for row in bank:
            if "1" not in row:
                continue
            devices = row.count("1")
            res += prev_devices * devices
            prev_devices = devices
        return res