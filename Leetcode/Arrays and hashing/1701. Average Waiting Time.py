from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        done, waiting = 0, 0
        for arrival, t in customers:
            if done < arrival:
                done = arrival
            done += t
            waiting += done - arrival
        return waiting / len(customers)