def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache: # 캐시에 있는 경우 (cache hit)
            answer += 1
            cache.remove(city) # 캐시에서 해당 도시를 제거
            cache.append(city) # 캐시의 마지막에 추가 (가장 최근에 사용)
        else: # 캐시에 없는 경우 (cache miss)
            answer += 5
            if cacheSize != 0: # 캐시사이즈가 0이 아닌 경우에만 캐시에 접근할 것
                if len(cache) == cacheSize: # 캐시가 꽉 찬 경우
                    cache.pop(0) # 가장 오래된 항목 삭제
                cache.append(city) # 캐시의 마지막에 추가
    return answer