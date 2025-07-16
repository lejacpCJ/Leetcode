class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        Returns the length of the longest valid subsequence in nums.
        A valid subsequence has all consecutive pairs with the same parity sum.
        """
        # Count of odd numbers in nums
        odd_count = 1 if nums[0] % 2 == 1 else 0
        # Count of even numbers in nums
        even_count = 0 if nums[0] % 2 == 1 else 1
        # Length of the longest alternating parity subsequence
        max_alternating = 1
        # Track the last number in the current alternating sequence
        last_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1
            else:
                even_count += 1

            # If parity changes, extend the alternating sequence
            if nums[i] % 2 != last_num % 2:
                max_alternating += 1
                last_num = nums[i]

        # The answer is the maximum among all possible valid subsequence types
        return max(odd_count, even_count, max_alternating)