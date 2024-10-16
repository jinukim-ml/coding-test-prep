import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ''
        consec = [0, 0, 0]
        cnt = []
        for i, num in enumerate([a,b,c]):
            if num > 0:
                heapq.heappush(cnt, (-num, i))
        
        while cnt:
            temp = []
            remaining, idx = heapq.heappop(cnt)

            while cnt and consec[idx] == 2:
                heapq.heappush(temp, (remaining, idx))
                remaining, idx = heapq.heappop(cnt)
            if consec[idx] == 2:
                break
            else:
                consec[(idx+1)%3] = 0
                consec[(idx+2)%3] = 0
                consec[idx] += 1
                ans += chr(idx + 97)

                remaining += 1
                if remaining < 0:
                    heapq.heappush(cnt, (remaining, idx))
                while temp:
                    heapq.heappush(cnt, heapq.heappop(temp))
        return ans