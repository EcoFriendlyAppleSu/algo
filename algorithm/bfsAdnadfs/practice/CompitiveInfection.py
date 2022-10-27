'''
문제 : 경쟁적 전염
내가 푼 문제는 80%만 맞췄다. 시간을 고려하지 않았기 때문
'''
from collections import deque

n, k = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
board = []
data = []


# dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            # 시간 값을 갖게 Setting
            data.append((board[i][j], 0 , i, j))

time, positionX, positionY = map(int, input().split())

data.sort()
queue = deque(data)

while queue:
    virus, sec, x, y = queue.popleft()
    if sec == time:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                queue.append((board, sec + 1, nx, ny))


# virusStartList = [(-1, -1)] * (k + 1)
#
#
# # virus List SetUp
# for start in range(1, k + 1):
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == start:
#                 virusStartList[start] = (i, j)
#
# print(virusStartList)
# print(board[0][0])
# def bfs(board, time, virusList):
#     queue = deque(virusList)
#
#     # 시간 만큼 돌립니다.
#     for i in range(time):
#         now = queue.popleft()
#         x, y = now
#         for j in range(4):
#             nx = x + dx[j]
#             ny = y + dy[j]
#             if 0 <= nx and nx < n and 0 <= ny and ny < n:
#                 if board[nx][ny] == 0:
#                     board[nx][ny] = board[x][y] # 바이러스 전이
#                     queue.append((nx,ny))
#
#     return board

print(board)
print(board[positionX-1][positionY-1])
print(board[2][2])

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2
