# https://school.programmers.co.kr/learn/courses/15009/lessons/121688

import heapq

def solution(ability, number):
    h = []
    for a in ability:
        heapq.heappush(h, a)
    
    for n in range(number):
        a, b = heapq.heappop(h), heapq.heappop(h)
        heapq.heappush(h, a + b)
        heapq.heappush(h, a + b)
    return sum(h)