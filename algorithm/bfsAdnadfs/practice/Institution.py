'''
문제 : 연구소
bfs 로 접근해봤는데 아닌가
'''

from itertools import combinations
import copy

n, m = map(int, input().split())
board = []
zeroList = []
result = 0

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 0:
            zeroList.append((i, j))

def bfs(walls, copyBoard):
    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0
    for wall in walls:
        wx, wy = wall
        copyBoard[wx][wy] = 1
    for nn in range(n):
        for mm in range(m):
            if copyBoard[nn][mm] == 2:
                queue.append((nn, mm))
                while queue:
                    xx, yy = queue.pop()
                    for i in range(4):
                        nx = xx + dx[i]
                        ny = yy + dy[i]
                        if 0 <= nx < n and 0 <= ny < m:
                            if copyBoard[nx][ny] == 0:
                                copyBoard[nx][ny] = 2
                                queue.append((nx, ny))
    for row in range(n):
        result += copyBoard[row].count(0)
    return result

answer = 0

# 벽 3개 == i
for i in list(combinations(zeroList, 3)):
    temp = bfs(i, copy.deepcopy(board))
    if answer < temp:
        answer = temp

print(answer)

# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2
