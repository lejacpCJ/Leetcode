from typing import List
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        lake_last_rain = dict()
        dry_days = []

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                ans[i] = 1  # Default, will be updated if needed
            else:
                if lake in lake_last_rain:
                    # Find a dry day after last rain on this lake
                    idx = bisect.bisect_right(dry_days, lake_last_rain[lake])
                    if idx == len(dry_days):
                        return []
                    dry_idx = dry_days[idx]
                    ans[dry_idx] = lake
                    dry_days.pop(idx)
                lake_last_rain[lake] = i
        return ans