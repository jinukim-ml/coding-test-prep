import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        book = set()
        cnt = 0
        h = [1]
        heapq.heapify(h)
        while cnt < n:
            ans = heapq.heappop(h)
            if ans not in book:
                book.add(ans)
                cnt += 1
                heapq.heappush(h, ans*2)
                heapq.heappush(h, ans*3)
                heapq.heappush(h, ans*5)

        return ans