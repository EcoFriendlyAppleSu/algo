# 음료수 얼려 먹기

N, M = map(int, input().split())
board = [ list(map(int, input())) for _ in range(N)]
print(board)
count = 0

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# def dfs(x, y):
#     board[x][y] == 1
#
#     for direction in range(4):
#         nx = x + dx[direction]
#         ny = y + dy[direction]
#         if 0 <= nx <= N and 0 <= ny < M:
#             board[nx][ny] = 1
#             dfs(nx, ny)
#
#
# for i in range(N): #N
#     for j in range(M): #M
#         if board[i][j] == 0:
#             dfs(i, j)
#             count += 1


def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if board[x][y] == 0:
        board[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1
print(count)


# 4 5
# 00110
# 00011
# 11111
# 00000