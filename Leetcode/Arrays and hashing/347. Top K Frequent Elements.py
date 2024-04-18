from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        frq = Counter(nums)
        for item in frq.most_common(k):
            answer.append(item[0])
        return answer