from typing import List
import collections

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # Sort events by timestamp, OFFLINE before MESSAGE at same timestamp
        events = sorted(events, key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        mentions = [0] * numberOfUsers
        status = [1] * numberOfUsers  # 1 = online, 0 = offline
        offline_queue = collections.deque()  # (user_id, online_time)

        for event in events:
            msg_type, time, mention_str = event
            time = int(time)
            # Restore users who should be online by now
            while offline_queue and offline_queue[0][1] <= time:
                off_id, _ = offline_queue.popleft()
                status[off_id] = 1

            if msg_type == "MESSAGE":
                if mention_str == "HERE":
                    for i, stat in enumerate(status):
                        if stat == 1:
                            mentions[i] += 1
                elif mention_str == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                else:
                    ids = mention_str.split()
                    for idx in ids:
                        idx_num = int(idx[2:])
                        mentions[idx_num] += 1
            else:  # OFFLINE
                idx = int(mention_str)
                status[idx] = 0
                offline_queue.append((idx, time + 60))

        return mentions