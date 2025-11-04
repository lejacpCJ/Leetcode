class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)
            # Sort by frequency descending, then value descending
            top = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            # Get the set of top x elements
            top_x = set([val for val, cnt in top[:x]])
            # Sum only occurrences of top x elements
            s = sum(num for num in window if num in top_x)
            answer.append(s)
        return answer