class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        lst = [0] * k
        for i in range(len(energy)):
            idx = i % k
            lst[idx] = max(lst[idx] + energy[i], energy[i])
        return max(lst)