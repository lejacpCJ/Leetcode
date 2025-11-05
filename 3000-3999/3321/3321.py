from sortedcontainers import SortedList
from collections import defaultdict
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        # 'selected' keeps the top x most frequent (freq, value) pairs in the current window
        selected = SortedList()
        # 'waitlist' keeps the rest of the candidates not in top x
        waitlist = SortedList()
        # 'freq' maps each value to its frequency in the current window
        freq = defaultdict(int)
        # 'skill_sum' is the sum of all occurrences of the top x elements in the window
        skill_sum = 0

        def remove_candidate(cand):
            # Remove a candidate (freq, value) from waitlist or selected
            nonlocal skill_sum
            if cand in waitlist:
                # If candidate is in waitlist, just remove it
                waitlist.remove(cand)
                return
            if cand in selected:
                # If candidate is in selected, remove and update skill_sum
                selected.remove(cand)
                skill_sum -= cand[0] * cand[1]
                # After removal, promote the next best candidate from waitlist if available
                if waitlist:
                    new_selection = waitlist[-1]  # max of waitlist (highest freq, highest value)
                    waitlist.remove(new_selection)
                    selected.add(new_selection)
                    skill_sum += new_selection[0] * new_selection[1]

        def add_candidate(cand):
            # Add a candidate (freq, value) to selected and update skill_sum
            nonlocal skill_sum
            selected.add(cand)
            skill_sum += cand[0] * cand[1]
            # If selected exceeds x, demote the least frequent (and smallest value) to waitlist
            if len(selected) > x:
                rejection = selected[0]  # min of selected (lowest freq, lowest value)
                selected.remove(rejection)
                skill_sum -= rejection[0] * rejection[1]
                waitlist.add(rejection)

        for i in range(n):
            # Add the new element at position i to the window
            cand = (freq[nums[i]], nums[i])
            if freq[nums[i]] > 0:
                # If this value already exists, remove its old candidate before updating frequency
                remove_candidate(cand)
            freq[nums[i]] += 1
            cand = (freq[nums[i]], nums[i])
            # Add the updated candidate to selected/waitlist
            add_candidate(cand)

            if i >= k:
                # Remove the element that is sliding out of the window
                out_idx = i - k
                cand = (freq[nums[out_idx]], nums[out_idx])
                remove_candidate(cand)
                freq[nums[out_idx]] -= 1
                if freq[nums[out_idx]] > 0:
                    # If the outgoing value still exists in the window, re-add its updated candidate
                    cand = (freq[nums[out_idx]], nums[out_idx])
                    add_candidate(cand)

            if i >= k - 1:
                # When the window is full, record the current x-sum
                ans.append(skill_sum)
        return ans