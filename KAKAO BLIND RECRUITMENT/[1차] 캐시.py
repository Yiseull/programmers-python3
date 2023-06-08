from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0: return len(cities) * 5

    answer = 0
    HIT = 1
    MISS = 5
    cache = deque()

    for city in cities:
        city = city.lower()

        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += HIT
            continue

        if cacheSize == len(cache):
            cache.popleft()
        cache.append(city)
        answer += MISS

    return answer