n, m, k = map(int, input().split())
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))
runners = []
for _ in range(m):
    r, c = map(int, input().split())
    maze[r - 1][c - 1] += 11
    runners.append((r - 1, c - 1))
exitr, exitc = map(int, input().split())

exitr, exitc = exitr - 1, exitc - 1
maze[exitr][exitc] = 23


def find_square(r, c):
    size = 0
    if exitr == r:
        size = abs(exitc - c)
        minc, maxc = min(exitc, c), max(exitc, c)
        minr, maxr = r - size, r
        while minr < 0:
            minr += 1
            maxr += 1
    elif exitc == c:
        size = abs(exitr - r)
        minr, maxr = min(exitr, r), max(exitr, r)
        minc, maxc = c - size, c
        while minc < 0:
            minc += 1
            maxc += 1
    else:
        if abs(exitr - r) > abs(exitc - c):
            size = abs(exitr - r)
            minr, maxr = min(exitr, r), max(exitr, r)
            minc, maxc = max(exitc, c) - size, max(exitc, c)
            while minc < 0:
                minc += 1
                maxc += 1
        else:
            size = abs(exitc - c)
            minc, maxc = min(exitc, c), max(exitc, c)
            minr, maxr = max(exitr, r) - size, max(exitr, r)
            while minr < 0:
                minr += 1
                maxr += 1
    return minr, minc, maxr, maxc, size + 1


def rotate_square(lr, lc, rr, rc, size):
    tmp = [[0 for _ in range(size)] for _ in range(size)]
    for r in range(size):
        for c in range(size):
            tmp[r][c] = maze[lr + size - 1 - c][lc + r]
            if 0 < tmp[r][c] < 10:
                tmp[r][c] -= 1
    for r in range(size):
        for c in range(size):
            maze[lr + r][lc + c] = tmp[r][c]


movesum = 0


def run(k):
    global movesum
    global runners, exitr, exitc
    for time in range(k):
        # print("step ", time)
        # print(runners, exitr, exitc)
        # for m in maze:
        #     print(m)
        # print()
        tmp = []
        # 참가자 이동
        while runners:
            r, c = runners.pop(0)
            m = abs(exitr - r) + abs(exitc - c)
            mr, mc = r, c
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if maze[nr][nc] == 0 or maze[nr][nc] >= 10:  # 벽이 아니라면
                        if abs(exitr - nr) + abs(exitc - nc) < m:
                            m = abs(exitr - nr) + abs(exitc - nc)
                            mr, mc = nr, nc
                        elif abs(exitr - nr) + abs(exitc - nc) == m:
                            if abs(r - nr) > 0:
                                m = abs(exitr - nr) + abs(exitc - nc)
                                mr, mc = nr, nc
            movesum += abs(r - mr) + abs(c - mc)
            maze[r][c] -= 11
            if mr != exitr or mc != exitc:
                maze[mr][mc] += 11
                tmp.append((mr, mc))



        if len(tmp) == 0:
            return

        # 정사각형 찾기
        minlr, minlc, minrr, minrc, minsize = n, n, n, n, 1000
        for tr, tc in tmp:
            lr, lc, rr, rc, size = find_square(tr, tc)
            if minsize > size:
                minlr, minlc, minrr, minrc, minsize = lr, lc, rr, rc, size
            elif minsize == size:
                if minlr > lr:
                    minlr, minlc, minrr, minrc, minsize = lr, lc, rr, rc, size
                elif minlr == lr:
                    if minlc > lc:
                        minlr, minlc, minrr, minrc, minsize = lr, lc, rr, rc, size
        # print(tmp)
        # print("rotate >> ", minlr, minlc, minrr, minrc, minsize)
        rotate_square(minlr, minlc, minrr, minrc, minsize)
        for r in range(n):
            for c in range(n):
                if maze[r][c] >= 10:
                    if maze[r][c] == 23:
                        exitr, exitc = r, c
                    else:
                        for tt in range(maze[r][c] // 11):
                            runners.append((r, c))

        # print(runners, exitr, exitc)
        # for m in maze:
        #     print(m)
        # print()


run(k)
print(movesum)
print(exitr + 1, exitc + 1)