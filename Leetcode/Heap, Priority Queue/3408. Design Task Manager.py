import heapq

class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.task_ids = {}
        self.priorities = []
        for u, t, p in tasks:
            self.task_ids[-t] = [-p, u]
            heapq.heappush(self.priorities, [-p, -t, u])
    
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_ids[-taskId] = [-priority, userId]
        heapq.heappush(self.priorities, [-priority, -taskId, userId])
    
    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task_ids[-taskId][1]
        self.task_ids[-taskId][0] = -newPriority
        heapq.heappush(self.priorities, [-newPriority, -taskId, userId])

    def rmv(self, taskId: int) -> None:
        self.task_ids.pop(-taskId)

    def execTop(self) -> int:
        res = -1
        while self.priorities:
            p, t, u = heapq.heappop(self.priorities)
            if t in self.task_ids and p == self.task_ids[t][0] and u == self.task_ids[t][1]:
                self.task_ids.pop(t)
                res = u
                break
        return res