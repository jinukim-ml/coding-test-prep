import heapq

class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        ins = []
        outs = []
        available = [i for i in range(len(times))]
        book = {}
        heapq.heapify(available)
        for i, (arr, lea) in enumerate(times):
            heapq.heappush(ins, (arr, i))
            heapq.heappush(outs, (lea, i))

        while ins:
            while outs[0][0] <= ins[0][0]:
                _, fren = heapq.heappop(outs)
                heapq.heappush(available, book.pop(fren))
            
            _, fren = heapq.heappop(ins)
            seat = heapq.heappop(available)
            if fren == targetFriend:
                return seat
            else:
                book[fren] = seat