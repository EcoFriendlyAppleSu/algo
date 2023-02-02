'''
백준 문제 : 16234
'''

from collections import deque

n, l, r = map(int, input().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
board = []
day = 0
for _ in range(n):
    board.append(list(map(int, input().split())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    contry = []
    contry.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and l <= abs(board[x][y] - board[nx][ny]) <= r:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    contry.append((nx, ny))
    return contry

while True:
    visited = [[False] * n for _ in range(n)]
    move = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                unionContry = bfs(i,j)
                if 1 < len(unionContry):
                    move = True
                    flatPopulation = sum([board[x][y] for x, y in unionContry]) // len(unionContry)
                    for x, y in unionContry:
                        board[x][y] = flatPopulation
    if not move: # move == False
        break
    else:
        day += 1
print(day)
'''
# dfs로 문제를 해결해봅시다.
n, l, r = map(int, input().split())
time = 0
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfsFirst(x,y, unionCount):

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if l <= (board[nx][ny] - board[x][y]) <= r:
                temp = board[x][y] + board[nx][ny]
                board[x][y] = temp
                board[nx][ny] = temp
                dfsFirst(nx,ny,unionCount + 1)
    return None

def dfsSecond(x,y, unionCount, standardValue):

    board[x][y] = standardValue / unionCount
    visited[x][y] = False

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == standardValue:
                dfsSecond(nx,ny, unionCount, standardValue)

    return None

while True:

    visited = [[False] * n for _ in range(n)]
    unionCount = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                dfsFirst(i,j,unionCount)

    if unionCount == 1:
        break

    time += 1

    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                standardValue = board[i][j]
                dfsSecond(i,j, unionCount, standardValue)
print(time)

'''

'''
2 20 50
50 30
20 40
'''