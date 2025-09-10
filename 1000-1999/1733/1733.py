from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_set = [set(l) for l in languages]
        need_fix = set()

        for u, v in friendships:
            if not (lang_set[u-1] & lang_set[v-1]):
                need_fix.add(u-1)
                need_fix.add(v-1)

        res = float('inf')

        for i in range(1, n+1):
            count = 0
            for user in need_fix:
                if i not in lang_set[user]:
                    count += 1
            res = min(res, count)

        return res