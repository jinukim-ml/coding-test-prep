import heapq

class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        tables, food_names = set(), set()
        receipts = []
        for _, table, food in orders:
            tables.add(int(table))
            food_names.add(food)
            heapq.heappush(receipts, (int(table), food))

        res = [["0" for _ in range(len(food_names)+1)] for _ in range(len(tables)+1)]
        res[0][0] = "Table"
        mapping, idx = {}, 1
        for food in sorted(list(food_names)):
            res[0][idx] = food
            mapping[food] = idx
            idx += 1

        tables = sorted(list(tables))
        row = 1
        for t in tables:
            res[row][0] = str(t)
            while receipts and t == receipts[0][0]:
                _, food = heapq.heappop(receipts)
                col = mapping[food]
                res[row][col] = str(int(res[row][col]) + 1)
            row += 1
        return res