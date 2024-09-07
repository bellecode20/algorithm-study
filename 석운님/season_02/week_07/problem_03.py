import heapq

n, m, k, c = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]
jechoje = [[0 for _ in range(n)] for _ in range(n)]
global answer
answer = 0

def grow_tree():
    for r in range(n):
        for c in range(n):
            if grid[r][c] > 0:
                cnt = 0
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < n and 0 <= nc < n:
                        # 상하좌우에 제초제가 없고 벽이 없고 나무가 있으면 칸 수만큼
                        if grid[nr][nc] > 0 and jechoje[nr][nc] == 0:
                            cnt += 1
                grid[r][c] += cnt


def breed_tree():
    add = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            available_cnt = []
            cnt = 0
            if grid[r][c] > 0:
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < n and 0 <= nc < n:
                        # 상하좌우에 벽, 나무, 제초제가 없으면
                        if grid[nr][nc] == 0 and jechoje[nr][nc] == 0:
                            available_cnt.append((nr, nc))
                            cnt += 1
                for ar, ac in available_cnt:
                    add[ar][ac] += (grid[r][c] // cnt)

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0 and jechoje[r][c] == 0:
                grid[r][c] += add[r][c]


def put_jechoje():
    global answer
    dcrossr, dcrossc = [1, -1, -1, 1], [1, -1, 1, -1]  # 하우, 상좌, 상우, 하좌
    putted = [[0 for _ in range(n)] for _ in range(n)]
    maxh = []
    for sr in range(n):
        for sc in range(n):
            if grid[sr][sc] <= 0:
                heapq.heappush(maxh, (0, sr, sc))
            else:
                amount = grid[sr][sc]
                for i in range(4):
                    nr, nc = sr, sc
                    for kk in range(k):
                        nr, nc = nr + dcrossr[i], nc + dcrossc[i]
                        if nr < 0 or nr >= n or nc < 0 or nc >= n:
                            break
                        if grid[nr][nc] <= 0:
                            break
                        amount += grid[nr][nc]
                heapq.heappush(maxh, (-amount, sr, sc))
    amount, sr, sc = heapq.heappop(maxh)
    if grid[sr][sc] <= 0:
        jechoje[sr][sc] = c + 1
        return
    jechoje[sr][sc] = c + 1
    answer += grid[sr][sc]
    grid[sr][sc] = 0
    for i in range(4):
        nr, nc = sr, sc
        for kk in range(k):
            nr, nc = nr + dcrossr[i], nc + dcrossc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                break
            if grid[nr][nc] <= 0:
                jechoje[nr][nc] = c + 1
                break
            jechoje[nr][nc] = c + 1
            answer += grid[nr][nc]
            grid[nr][nc] = 0
    # print(-amount)

def remove_jechoje():
    for r in range(n):
        for c in range(n):
            if jechoje[r][c] > 0:
                jechoje[r][c] -= 1


def print_grid():
    for g in grid:
        print(g)
    print()
    for j in jechoje:
        print(j)
    print()


for year in range(1, m + 1):
    grow_tree()  # 성장
    # print_grid()
    breed_tree()  # 번식
    # print_grid()
    put_jechoje()  # 제초제 놓기
    # print_grid()
    remove_jechoje()
    # print_grid()
print(answer)