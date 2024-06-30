
import sys
sys.setrecursionlimit(10**9)

def solution(n, m, x, y, r, c, k):
    global ans
    ans = "z"
    mink = abs(x - r) + abs(y - c)
    if mink > k or (k - mink) % 2 == 1: # k번 이동해서는 풀 수 없는 경우
        return "impossible"
    
    d = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}
    dr, dc = [1, 0, 0, -1], [0, -1, 1, 0]

    def dfs(sr, sc, dist, s): # 현재 위치 sr, sc, 지금까지 온 거리, 과거 행보
        global ans
        # 만약 이동하는 도중 k번째에 도착지에 도착할 수 없게 되면 return
        if dist + abs(sr - (r - 1)) + abs(sc - (c - 1)) > k: 
            return
        # k번째에 도착지에 도착하면 ans 업데이트
        if dist == k and (sr, sc) == (r-1, c-1): 
            ans = s
            return
        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if s < ans: # 사전순으로
                    dfs(nr, nc, dist + 1, s + d[i])
    dfs(x-1, y-1, 0, "")
    
    return ans