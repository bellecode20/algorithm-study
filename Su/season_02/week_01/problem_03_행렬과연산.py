# 풀이 참고: https://www.youtube.com/watch?v=8MpZYg4BqTI
from collections import deque
def solution(rc, operations):
    start = deque()
    mid = deque()
    end = deque()
    for i in rc: # row 마다 추가하기
        start.append(i[0])
        mid.append(deque(i[1:len(i)-1]))
        end.append(i[len(i)-1])
    for op in operations:
        if op == "Rotate":
            mid[0].appendleft(start.popleft())
            end.appendleft(mid[0].pop())
            mid[len(mid)-1].append(end.pop())
            start.append(mid[len(mid)-1].popleft())
        elif op == "ShiftRow":
            start.rotate()
            mid.rotate()
            end.rotate()
    answer = []
    for i in range(len(rc)):
        row = [start[i]] + list(mid[i]) + [end[i]]
        answer.append(row)
    return answer