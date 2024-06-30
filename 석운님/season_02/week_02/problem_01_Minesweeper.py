from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dd = [(-1, 0),(-1, -1),(0, -1),(1, -1),(1, 0),(1, 1),(0, 1),(-1, 1)]
        n, m = len(board), len(board[0])
        sr, sc =  click[0], click[1]
        if board[sr][sc] == 'M':
            board[sr][sc] = 'X'
        elif board[sr][sc] == 'E':
            q = deque()
            cnt = 0
            for j in range(8):
                if 0 <= sr + dd[j][0] < n and 0 <= sc + dd[j][1] < m:
                    if board[sr + dd[j][0]][sc + dd[j][1]] == 'M':
                        cnt += 1
            if cnt == 0: # 'E'를 'B'로 바꾸고 주변 'E'를 bfs로 계속 탐색한다.
                board[sr][sc] = 'B'
                q.append((sr, sc))
            else:
                board[sr][sc] = str(cnt) # 그냥 주변 지뢰 숫자를 넣는다
            while q:
                r, c = q.popleft()
                for i in range(8):
                    nr, nc = r + dd[i][0], c + dd[i][1]
                    if 0 <= nr < n and 0 <= nc < m:
                        if board[nr][nc] == 'E':
                            cnt = 0
                            for j in range(len(dd)): # 주변 폭탄의 개수를 확인한다
                                if 0 <= nr + dd[j][0] < n and 0 <= nc + dd[j][1] < m:
                                    if board[nr + dd[j][0]][nc + dd[j][1]] == 'M':
                                        cnt += 1
                            if cnt == 0:
                                board[nr][nc] = 'B' # 주변에 폭탄이 없으면 'B'로 바꾸고 계속 탐색한다
                                q.append((nr, nc))
                            else:
                                board[nr][nc] = str(cnt) # 주변에 폭탄이 있으면 폭탄의 수를 넣는다
        for b in board:
            print(b)
        print()
        return board