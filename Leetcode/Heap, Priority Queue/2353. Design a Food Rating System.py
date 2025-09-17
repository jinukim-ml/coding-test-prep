from collections import defaultdict
import heapq

class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.foods = {}
        self.categories = defaultdict(list)
        for i in range(len(foods)):
            self.foods[foods[i]] = [ratings[i], cuisines[i]]
            heapq.heappush(self.categories[cuisines[i]], [-ratings[i], foods[i]])
    def changeRating(self, food: str, newRating: int) -> None:
        self.foods[food][0] = newRating
        cuisine = self.foods[food][1]
        heapq.heappush(self.categories[cuisine], [-newRating, food])
    def highestRated(self, cuisine: str) -> str:
        while self.categories[cuisine] and -self.categories[cuisine][0][0] != self.foods[self.categories[cuisine][0][1]][0]:
            heapq.heappop(self.categories[cuisine])
        return self.categories[cuisine][0][1]