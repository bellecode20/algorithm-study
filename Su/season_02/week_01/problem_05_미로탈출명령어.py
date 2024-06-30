import sys

def solution(n, m, x, y, r, c, k): 
    # n, m 크기 격자 미로
    # (x, y) 출발, (r, c) 도착
    # k만큼 이동 가능
    sys.setrecursionlimit(5000)
    # dx, dy, direction 모두 d -> l -> r -> u 순으로 세팅한다.
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    direction = ["d", "l", "r", "u"]
    
    distance = abs(x - r) + abs(y - c) # 현재 위치에서 도착점까지의 절대거리
    if (distance > k) or ((k % 2) != (distance % 2)):
        return "impossible"
    
    def dfs(cur_x, cur_y, dist):
        # 도착한 경우
        if (cur_x == r) and (cur_y == c) and dist == k:
            return True
        # k만큼 움직였는데 도착하지 못한 경우
        if dist == k:
            return False
        # 격자 바깥으로 벗어난 경우
        elif (cur_x <= 0) or (cur_y <= 0) or (cur_x > n) or (cur_y > m):
            return False
        # 남은 거리로는 현재위치에서 목적지에 도달할 수 없는 경우
        elif (abs(cur_x - r) + abs(cur_y - c)) > (k - dist):
            return False
        
        # 4가지 방향으로 탐색(d,l,r,u 순)
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            route.append(direction[i])
            if dfs(next_x, next_y, dist + 1): # 또 4가지 방향 탐색
                return True
            route.pop() # 조건 충족못하는 이동이었으므로 삭제한다.
        
        # 모든 방향 시도했는데 return True가 가능하지 않음 -> return False
        return False
    
    route = []
    if dfs(x, y, 0):
        return "".join(route)
    else:
        return "impossible"
    