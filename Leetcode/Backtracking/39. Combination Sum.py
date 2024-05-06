from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.res = []
        self.target = target
        self.DFS(0, 0, [])
        return self.res

    def DFS(self, idx: int, agg: int, curr: List[int]):
        if agg == self.target:
            self.res.append(curr[:])
        elif agg < self.target:
            for j in range(idx, len(self.candidates)):
                curr.append(self.candidates[j])
                self.DFS(j, agg + self.candidates[j], curr[])
                curr.pop()