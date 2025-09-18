import heapq

class TaskManager:
    def __init__(self, tasks):
        self.task_to_user_priority = {}
        self.task_heap = []
        for user, task, priority in tasks:
            self.task_to_user_priority[task] = (user, priority)
            heapq.heappush(self.task_heap, (-priority, -task))

    def add(self, userId, taskId, priority):
        self.task_to_user_priority[taskId] = (userId, priority)
        heapq.heappush(self.task_heap, (-priority, -taskId))

    def edit(self, taskId, newPriority):
        user, _ = self.task_to_user_priority[taskId]
        self.task_to_user_priority[taskId] = (user, newPriority)
        heapq.heappush(self.task_heap, (-newPriority, -taskId))

    def rmv(self, taskId):
        if taskId in self.task_to_user_priority:
            del self.task_to_user_priority[taskId]

    def execTop(self):
        while self.task_heap:
            neg_p, neg_t = heapq.heappop(self.task_heap)
            priority, task = -neg_p, -neg_t
            if task in self.task_to_user_priority and self.task_to_user_priority[task][1] == priority:
                user = self.task_to_user_priority[task][0]
                del self.task_to_user_priority[task]
                return user
        return -1