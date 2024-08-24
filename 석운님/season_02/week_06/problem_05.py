from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    maxcnt = len(queue1)*3
    while True:
        if s1 < s2:
            tmp = q2.popleft()
            q1.append(tmp)
            s1 += tmp
            s2 -= tmp
            answer += 1
        elif s1 > s2:
            tmp = q1.popleft()
            q2.append(tmp)
            s1 -= tmp
            s2 += tmp
            answer += 1
        else:
            break
        if answer >= maxcnt:
            return -1
    return answer