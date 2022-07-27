# 게임 맵 최단거리 가야할 방향이 있는 문제
from collections import deque

# using dfs or bfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue: # queue가 끝날 때까지 순회한다.
        x, y = queue.popleft() # 방문한 곳의 좌표를 꺼내고

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 방문하려고 하는 곳이 board(여기선 maps)의 범위 바깥으로 벗어난다면 다음 좌표로 이동
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            # 방문한 곳의 길이 뚫려있지 않다면
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[len(maps) -1][len(maps[0]) - 1]

def solution(maps):
    answer = 0
    answer = bfs(0,0)

    return -1 if answer == 1 else answer

if __name__ == '__main__':
    maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
    visited = [[False for _ in range(len(maps))] for _ in range(len(maps[0]))]
    print(visited)
    # print(solution(maps))
