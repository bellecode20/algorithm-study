from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N//2 # 나중에 회전할 때 사용할 중앙 인덱스 값

# 1회전, 점수구하기 -> 2회전, 점수구하기 -> 3회전, 점수구하기 반복.

def bfs(start_row, start_col):
    queue = deque()

    queue.append((start_row, start_col))
    visited[start_row][start_col] = True
    groups[-1].add((start_row, start_col)) # 칸 추가

    while queue:
        cur_row, cur_col = queue.popleft()
        # 네방향으로 탐색
        dr = [-1, 0, 0, 1]
        dc = [0, -1, 1, 0]
        for i in range(4):
            nr = cur_row + dr[i]
            nc = cur_col + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if visited[nr][nc]:
                continue
            if arr[nr][nc] != arr[cur_row][cur_col]: # 다른 값이면 넘기기
                continue
            visited[nr][nc] = True
            groups[-1].add((nr, nc))
            queue.append((nr, nc))

answer = 0
for k in range(4):
    # [1] 점수 구하기
    groups = [] # set()에 칸 저장 
    nums = [] # 그룹별 숫자 값
    # bfs로 방문하면서, 같은 그룹인 칸들 기록할 예정
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            groups.append(set()) # 방문안했고, 숫자 시작점찾음
            nums.append(arr[i][j]) # 숫자 값 기록
            bfs(i, j)
    
    CNT = len(nums)
    for i in range(0,CNT-1):
        for j in range(i+1, CNT):   # CNT개에서 2개 뽑는 가능한 모든 조합
            point = (len(groups[i])+len(groups[j]))*nums[i]*nums[j]  # 인접면 1개당 더해질 점수
            for ci,cj in groups[i]:
                for ni,nj in ((ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)):
                    if (ni,nj) in groups[j]:    # 인접한 좌표가 그룹j에 있다면 두 그룹은 인접
                        answer += point
    if k == 3:
        break
    
    # [2] 회전시키기: "+"반시계 회전, 부분사각형 시계방향
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        new_arr[M][i] = arr[i][M] # 가로줄 채우기. 기존 세로줄이었음
    for j in range(N):
        new_arr[j][M] = arr[M][N - j - 1] # 세로줄 채우기. 기존 가로줄이었음

    # 부분 사각형 시계 방향
    # 사각형 내 좌측 상단 칸을 기준으로 한다.
    for (s_row, s_col) in ((0, 0), (0, M+1), (M+1, 0), (M+1, M+1)):
        for i in range(M):
            for j in range(M):
                new_arr[s_row + i][s_col + j] = arr[s_row + M-j-1][s_col + i]
    arr = new_arr    


print(answer)