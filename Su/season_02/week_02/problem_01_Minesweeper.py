class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        def count_mines(x, y):
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and board[nx][ny] == 'M':
                    count += 1
            return count
        
        def dfs(x, y):
            if not is_valid(x, y) or board[x][y] != 'E': # "E"가 아닌 경우 이미 방문한 경우임
                return
            
            mine_count = count_mines(x, y)
            if mine_count == 0:
                board[x][y] = 'B'
                for dx, dy in directions:
                    dfs(x + dx, y + dy)
            else:
                board[x][y] = str(mine_count)
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            dfs(x, y)
        
        return board