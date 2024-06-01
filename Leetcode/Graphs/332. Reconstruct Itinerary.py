from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = defaultdict(list)
        for start, end in tickets:
            flights[start].append(end)
        for destination in flights.values():
            destination.sort(reverse=True)
        
        ans = []

        def dfs(origin):
            destinations = flights[origin]
            while destinations:
                next_dest = destinations.pop()
                dfs(next_dest)
            ans.append(origin)

        dfs('JFK')
        return ans[::-1]