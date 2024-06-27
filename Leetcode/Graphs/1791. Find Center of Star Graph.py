from typing import List
from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        table = defaultdict(int)
        for st, de in edges:
            table[st] += 1
            table[de] += 1

            if table[st] > 1:
                return st
            if table[de] > 1:
                return de