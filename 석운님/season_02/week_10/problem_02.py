from collections import deque

def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    # parent 배열에 같은 그룹을 대표하는 r, c, 그리고 그룹 크기를 저장한다
    parent = [[(-1, -1, -1) for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    for sr in range(n):
        for sc in range(m):
            if not visited[sr][sc] and land[sr][sc]==1:
                q = deque()
                arr = []
                q.append((sr, sc))
                visited[sr][sc] = True
                cnt = 0
                while q:
                    r, c = q.popleft()
                    cnt += 1
                    arr.append((r, c))
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < n and 0 <= nc < m:
                            if not visited[nr][nc] and land[nr][nc]==1:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                arr.sort()
                tr, tc = arr[0][0], arr[0][1]
                for r, c in arr:
                    parent[r][c] = (tr, tc, cnt)

    ans = 0
    for col in range(m):
        s = set()
        for row in range(n):
            if parent[row][col] not in s and parent[row][col] != (-1, -1, -1):
                s.add(parent[row][col])
        total = sum([a[2] for a in list(s)])
        ans = max(ans, total)
    return ans