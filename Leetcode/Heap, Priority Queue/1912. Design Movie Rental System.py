class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(list) # store (price, shop)
        self.rented = [] # store (price, shop, movie)
        self.movie_info = defaultdict(list) # self.movie_info[(shop, movie)] = [price: int, is_rented: bool]
        
        for s, m, p in entries:
            heapq.heappush(self.movies[m], (p,s))
            self.movie_info[(s, m)] = [p, False]

    def search(self, movie: int) -> List[int]:
        res = []
        buffer = deque()
        while self.movies[movie] and len(res) < 5:
            p, s = heapq.heappop(self.movies[movie])
            buffer.append((p,s))
            if not self.movie_info[(s, movie)][1]: # not rented
                res.append(s)
        while buffer:
            p, s = buffer.popleft()
            heapq.heappush(self.movies[movie], (p,s))
        return res

    def rent(self, shop: int, movie: int) -> None:
        p = self.movie_info[(shop, movie)][0]
        heapq.heappush(self.rented, (p, shop, movie))
        self.movie_info[(shop, movie)][1] = True

    def drop(self, shop: int, movie: int) -> None:
        self.movie_info[(shop, movie)][1] = False

    def report(self) -> List[List[int]]:
        res = []
        buffer = deque()
        seen = set()
        while self.rented and len(res) < 5:
            p, s, m = heapq.heappop(self.rented)
            if self.movie_info[(s,m)][1] and (m,s) not in seen:
                res.append([s, m])
                buffer.append((p, s, m))
                seen.add((m,s))
        while buffer:
            p, s, m = buffer.popleft()
            heapq.heappush(self.rented, (p, s, m))
        return res
