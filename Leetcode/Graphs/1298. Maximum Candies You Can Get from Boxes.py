from collections import deque

class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        visited = set()
        waitlist = set()
        keychain = set()
        q = deque()
        for box in initialBoxes:
            if status[box]:
                q.append(box)
            else:
                waitlist.add(box)
        
        while q:
            box = q.popleft()
            visited.add(box)
            for k in keys[box]:
                if k in visited:
                    continue
                if k in waitlist:
                    q.append(k)
                    waitlist.discard(k)
                else:
                    keychain.add(k)

            for next_box in containedBoxes[box]:
                if next_box in visited:
                    continue
                if status[next_box] or next_box in keychain:
                    q.append(next_box)
                else:
                    waitlist.add(next_box)

        res = 0
        for box in visited:
            res += candies[box]
        return res