
def solution(cacheSize, cities):
    '''
    작전: 최후발생이 가장 오래된 친구를 제거해야한다.
    
    '''
    cities = [i.lower() for i in cities]
    recent = {}
    answer = 0
    for i in range(len(cities)):
        city = cities[i]
        if city in recent:
            answer += 1
            recent[city] = i
            continue
        answer += 5
        recent[city] = i
        if len(recent)> cacheSize:
            del(recent[sorted(recent, key = lambda x: recent[x])[0]])

    return answer