# https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import OrderedDict

def solution(cacheSize: int, cities: list[str]) -> int:
    if cacheSize == 0:
        return len(cities) * 5
    cache = OrderedDict()
    ans, cnt = 0, 0
    
    for city in cities:
        c = city.lower()
        if c in cache:
            cache.move_to_end(c)
            ans += 1
        elif len(cache) == cacheSize:
            cache.popitem(last=False)
            ans += 5
        else:
            ans += 5
        cache[c] = cnt
        cnt += 1
    return ans