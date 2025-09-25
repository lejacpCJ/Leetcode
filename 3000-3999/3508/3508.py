from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.q = deque()  # stores (source, destination, timestamp)
        self.exists = set()  # set of (source, destination, timestamp) for duplicate check
        self.dest_times = defaultdict(list)  # destination -> sorted list of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.exists:
            return False
        # add packet
        self.q.append((source, destination, timestamp))
        self.exists.add(key)
        # because addPacket timestamps are non-decreasing globally, append keeps list sorted
        self.dest_times[destination].append(timestamp)
        # ensure memory limit: if exceeded, evict oldest once
        if len(self.q) > self.limit:
            # evict oldest
            src, dst, ts = self.q.popleft()
            self.exists.discard((src, dst, ts))
            lst = self.dest_times[dst]
            i = bisect.bisect_left(lst, ts)
            if i < len(lst) and lst[i] == ts:
                lst.pop(i)
            if not lst:
                del self.dest_times[dst]
        return True

    def forwardPacket(self):
        if not self.q:
            return []
        src, dst, ts = self.q.popleft()
        self.exists.discard((src, dst, ts))
        lst = self.dest_times[dst]
        i = bisect.bisect_left(lst, ts)
        if i < len(lst) and lst[i] == ts:
            lst.pop(i)
        if not lst:
            del self.dest_times[dst]
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_times:
            return 0
        lst = self.dest_times[destination]
        l = bisect.bisect_left(lst, startTime)
        r = bisect.bisect_right(lst, endTime)
        return r - l