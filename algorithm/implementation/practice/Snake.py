'''
문제 뱀
1, 특정 위치에서 오른쪽 혹은 왼쪽으로 회전 시 사용되는 방향 알고리즘 기억해두자
2, 위치를 기억하고 싶을 땐 리스트를 만들어 저장해서 사용해보자
'''

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

turnInfo = int(input())
for _ in range(turnInfo):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c): # #1
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1
    data[x][y] = 2  # 뱀 시작 값 2
    direction = 0  # 처음 동쪽을 바라봄
    time = 0  # 걸린 시간
    index = 0  # 다음에 회전할 정보
    snake = [(x, y)]  # 뱀의 몸을 나타내는 변수 #2
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2  # 뱀 머리 이동
                snake.append((nx, ny))
                snakeX, snakeY = snake.pop(0)
                data[snakeX][snakeY] = 0  # 뱀 이동 후 0으로 처리

            if data[nx][ny] == 1:
                data[nx][ny] = 2
                snake.append((nx, ny))

        else:
            time += 1
            break
        x, y = nx, ny
        time += 1

        if time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulate())

# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L