'''
백준 문제 : 2468
Recurisve Error 발생
'''
import  sys

input = sys.stdin.readline
sys.getrecursionlimit(10**6)
n = int(input())
answer = 0
result = 0
board = []
visited = []
boardMaxValue = 0

for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] > boardMaxValue:
            boardMaxValue = board[i][j]
print(boardMaxValue)
dx = [0,1,0,-1]
dy = [-1,0,1,0]

def dfs(x,y, visited, height):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and board[nx][ny] > height:
            dfs(nx,ny,visited, height)

# 100
for height in range(2, boardMaxValue+1):
    visited = [([False] * n) for x in range(n)] # N * N
    # N * N
    for i in range(n):
        for j in range(n):
            if board[i][j] > height and visited[i][j] == False:
                dfs(i,j,visited,height)
                answer += 1
    if answer >= result:
        result = answer

    answer = 0
if result == 0:
    result = 1
print(result)
# 100 ( (100*100) + (100 * 100 * 4)) 입니다.
'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''
