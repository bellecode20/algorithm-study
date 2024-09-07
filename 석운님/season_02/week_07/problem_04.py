from collections import deque

n = int(input())
global grid
grid=[]
for _ in range(n):
    grid.append(list(map(int, input().split())))


def rotate_middle():
    global grid
    newgrid = [[grid[i][j] for j in range(n)] for i in range(n)]
    for i in range(n // 2):
        newgrid[n // 2][i] = grid[i][n // 2]
    for i in range(n // 2):
        newgrid[n - 1 - i][n // 2] = grid[n // 2][i]
    for i in range(n // 2):
        newgrid[n // 2][n - 1 - i] = grid[n - 1 - i][n // 2]
    for i in range(n // 2):
        newgrid[i][n // 2] = grid[n // 2][n - 1 - i]
    grid = [ng[:] for ng in newgrid]

def rotate_corner(sr, sc):
    global grid
    newgrid = [[0 for _ in range(n // 2)] for _ in range(n // 2)]
    for r in range(n // 2):
        for c in range(n // 2):
            # print(r, c, "<===", sr + (n // 2 - 1 - c), sc + r, grid[sr + (n // 2 - 1 - c)][sc + r])
            newgrid[r][c] = grid[sr + (n // 2 - 1 - c)][sc + r]
    for r in range(n // 2):
        for c in range(n // 2):
            grid[sr + r][sc + c] = newgrid[r][c]


dr, dc = [0, 0, -1, 1], [1, -1, 0, 0]


def comb(l):
    result = []
    def dfs(i, arr):
        if len(arr) == 2:
            result.append(arr[:])
            return
        for j in range(i, l):
            dfs(j + 1, arr + [j])

    dfs(0, [])
    return result

answer = 0

def get_score():
    groups = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for sr in range(n):
        for sc in range(n):
            if not visited[sr][sc]:
                num = grid[sr][sc]
                visited[sr][sc] = True
                q = deque()
                group_components = set()
                q.append((sr, sc))
                cnt = 0
                while q:
                    r, c = q.popleft()
                    group_components.add((r, c))
                    cnt += 1
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < n and 0 <= nc < n:
                            if not visited[nr][nc] and grid[nr][nc] == num:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                groups.append((num, cnt, group_components))
    c = comb(len(groups))
    
    def get_same(a, b):
        cnt = 0
        for r, c in list(groups[a][2]):
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) in groups[b][2]:
                        cnt += 1
        return cnt

    score = 0
    for i in range(len(c)):
        a, b = c[i][0], c[i][1]
        total_blocks = groups[a][1] + groups[b][1]
        anum, bnum = groups[a][0], groups[b][0]
        same = get_same(a, b)
        score += total_blocks * anum * bnum * same
    return score


for turn in range(4):
    answer += get_score()
    if turn == 4:
        break
    # for g in grid:
    #     print(g)
    rotate_middle()
    rotate_corner(0, 0)
    rotate_corner(0, n // 2 + 1)
    rotate_corner(n // 2 + 1, 0)
    rotate_corner(n // 2 + 1, n // 2 + 1)
    # for g in grid:
    #     print(g)

print(answer)