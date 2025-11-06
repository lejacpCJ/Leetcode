from typing import List
from collections import defaultdict
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parents = [i for i in range(c+1)]
        online_status = [True] * (c+1)

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu != pv:
                if pu <= pv:
                    parents[pv] = pu
                else:
                    parents[pu] = pv

        for u, v in connections:
            union(u, v)

        min_in_component = defaultdict(list)
        for i in range(1, c+1):
            heapq.heappush(min_in_component[find(i)], i)

        res = []
        for op, x in queries:
            if op == 2:
                online_status[x] = False
            else:
                if online_status[x]:
                    res.append(x)
                else:
                    min_in_component_heap, notFound = min_in_component[find(x)], True
                    while min_in_component_heap:
                        station = min_in_component_heap[0]
                        if online_status[station]:
                            res.append(station)
                            notFound = False
                            break
                        heapq.heappop(min_in_component_heap)
                    if notFound:
                        res.append(-1)
        return res