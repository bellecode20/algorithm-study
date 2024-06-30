def solution(cacheSize, cities):
    if cacheSize == 0: return len(cities)*5
    answer = 0
    cache = []
    for i, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                a = cache.pop(0)
            cache.append(city)
    return answer
