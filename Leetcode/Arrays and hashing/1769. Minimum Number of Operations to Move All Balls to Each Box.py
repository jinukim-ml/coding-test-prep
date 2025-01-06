class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        res = []
        for i in range(len(boxes)):
            moves = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    moves += abs(j - i)
            res.append(moves)
        return res