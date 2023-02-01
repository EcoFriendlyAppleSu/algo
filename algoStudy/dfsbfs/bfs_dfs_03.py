'''
백준 문제 : 18405
상태 값을 저장하는 생각을 하지 못했습니다.
'''

from collections import deque
# from collections import defaultdict
#
# n, k = list(map(int, input().split()))
# board = []
# virous = defaultdict(deque)
#
# dx = [0,0,-1,0]
# dy = [1,-1,0,0]
#
# # making board
# for i in range(n):
#     board.append(list(map(int, input().split())))
#
# sec, xPos, yPos = list(map(int, input().split()))
#
# # defaultDict x,y position inject
# for v in range(1, k+1):
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == v:
#                 virous[v].append((i,j))
#                 break
#
# def bfs(virous, virousNumber):
#
#     while virous[virousNumber]:
#         popleft = virous[virousNumber].popleft()
#
#         for direction in range(4):
#             nx = popleft[0] + dx[direction]
#             ny = popleft[1] + dy[direction]
#
#             if 0 <= nx < n and 0 <= ny < n:
#                 if board[nx][ny] == 0:
#                     board[nx][ny] = board[popleft[0]][popleft[1]]
#                     virous[virousNumber].append((nx,ny))
#
#     return virous
#
# for _ in range(sec):
#     for virousNumber in (1, k+1):
#         bfs(virous, virousNumber)
#
# print(virous[xPos, yPos])

n, k = map(int, input().split())
board = []
virous = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j]:
            virous.append((board[i][j], 0, i,j))

# 맨 앞에 값을 기준으로 정렬이됩니다.
virous.sort()

queue = deque(virous)

sec, xPos, yPos = map(int, input().split())
while queue:
    v,s,x,y = queue.popleft()
    if s == sec:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = v
                queue.append((v, s+1, nx, ny))

print(board[xPos-1][yPos-1])

'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2
'''