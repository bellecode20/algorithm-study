# https://school.programmers.co.kr/learn/courses/15009/lessons/121690


# import sys
# sys.setrecursionlimit(10**9)

# def solution(n, m, hole):
#     global mincnt
#     mincnt = int(10**9)
#     dr, dc = [1, 0], [0, 1] # 상, 우
#     grid = [[0]*(m + 1) for _ in range(n + 1)]
#     for h in hole:
#         grid[h[0]][h[1]] = 1
#     visited = [[False]*(m + 1) for _ in range(n + 1)]
#     def dfs(r, c, is_use, cnt):
#         global mincnt
#         visited[r][c] = True
#         #print(r, c, is_use, cnt, mincnt)
#         if (r, c) == (n, m):
#             if cnt < mincnt:
#                 mincnt = cnt
#             return
#         if cnt > mincnt:
#             return
#         if grid[r][c] == 1:
#             return
        
#         if not is_use:
#             for i in range(2):
#                 nr, nc = r + 2*dr[i], c + 2*dc[i]
#                 if (1 <= nr <= n) and (1 <= nc < m):
#                     if not visited[nr][nc]:
#                         dfs(nr, nc, True, cnt + 1)
        
#         for i in range(2):
#             nr, nc = r + dr[i], c + dc[i]
#             if (1 <= nr <= n) and (1 <= nc <= m):
#                 if not visited[nr][nc]:
#                     dfs(nr, nc, is_use, cnt + 1)
    
#     dfs(1, 1, False, 0)
#     if mincnt == int(10**9):
#         return -1
#     return mincnt


from collections import deque

def solution(n, m, hole):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    graph = [[0] * m for _ in range(n)]
    for a,b in hole:
        graph[a-1][b-1] = 1
    
    queue = deque() 
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)] # x,y,신발사용여부
    visited[0][0][False] = True 
    queue.append((0,0,False))
    L = 0
    
    while queue:
        
        for _ in range(len(queue)):
            x,y,used = queue.popleft()
                  
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][used] and graph[nx][ny] == 0:
                    if (nx,ny) == (n-1,m-1):
                        return L + 1
                    visited[nx][ny][used] = True
                    queue.append((nx,ny,used))
                    
                if not used: # 신발사용하면서 이동하기
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][used] and graph[nx][ny] == 0:
                        if (nx,ny) == (n-1,m-1):
                            return L + 1
                        visited[nx][ny][True] = True
                        queue.append((nx,ny,True))
        L += 1    
    return -1