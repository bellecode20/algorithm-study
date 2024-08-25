from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    answer = []
    flag = False
    scorediff = 0
    for cwr in combinations_with_replacement(range(11), n):
        rscore, ascore = 0, 0
        c = Counter(list(cwr))
        visit = [False for _ in range(11)]
        for key in c:
            visit[key] = True
            if info[10 - key] < c[key]:
                rscore += key
            else:
                ascore += key
        for i in range(11):
            if not visit[i] and info[10 - i] > 0:
                ascore += i
        if rscore > ascore and abs(rscore - ascore) > scorediff:
            flag = True
            scorediff = abs(rscore - ascore)
            tmp = [0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for key in c:
                tmp[10 - key] = c[key]
            answer = tmp[:]
        elif rscore > ascore and abs(rscore - ascore) == scorediff and scorediff != 0:
            tmp = [0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            origintmp = tmp[:]
            for key in c:
                tmp[10 - key] = c[key]
            if "".join(str(reversed(answer))) < "".join(str(reversed(tmp))):
                flag = True
                answer = tmp
    if not flag:
        return [-1]
    return answer