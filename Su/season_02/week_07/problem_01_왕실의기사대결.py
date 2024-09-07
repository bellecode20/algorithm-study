from collections import deque
N, M, Q = map(int, input().split())
EMPTY, TRAP, WALL = 0, 1, 2
arr = [[WALL]*(N+2)]+[[WALL]+list(map(int, input().split()))+[WALL] for _ in range(N)]+[[WALL]*(N+2)]
units = {}

init_k = [0] * (M+1) # 초기 체력 기록
for m in range(1, M+1):
    start_row, start_col, h, w, k = map(int, input().split())
    units[m] = [start_row, start_col, h, w, k]
    init_k[m] = k

def push_unit(start, direction):
    queue = deque()
    pset = set()
    damage = [0] * (M+1)
    queue.append(start)
    pset.add(start)

    while queue:
        cur_unit = queue.popleft()
        cur_row, cur_col, h, w, k = units[cur_unit]

        # 상 우 하 좌
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        nr, nc = cur_row + dr[direction], cur_col + dc[direction]
        for i in range(nr, nr + h):
            for j in range(nc, nc + w):
                if arr[i][j] == WALL:
                    return # 즉시 종료.
                if arr[i][j] == TRAP:
                    damage[cur_unit] += 1
        
        # 겹치는 유닛인 경우 큐에 넣어서 또 이동한다.
        for idx in units:
            if idx in pset: # 이미 움직일 대상이면 체크할 필요 없음
                continue
            tr, tc, th, tw, tk = units[idx]
            # 겹치는 경우
            if nr <= tr + th - 1 and nr + h - 1 >= tr and tc <= nc + w - 1 and nc <= tc + tw-1:
                queue.append(idx)
                pset.add(idx)
    damage[start] = 0

    for idx in pset:
        sr, sc, h, w, k = units[idx]
        if k <= damage[idx]:
            units.pop(idx) # 체력 고갈되면 삭제
        else:
            nr, nc = sr + dr[direction], sc + dc[direction]
            units[idx] = [nr, nc, h, w, k - damage[idx]]
            

for _ in range(Q):
    idx, direction = map(int, input().split())
    if idx in units: # 아직 보드판에 있는 기사인 경우만
        push_unit(idx, direction)

ans = 0
for idx in units:
    ans += init_k[idx]-units[idx][4]
print(ans)