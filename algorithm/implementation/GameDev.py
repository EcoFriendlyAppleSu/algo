# 게임 개발

N, M = map(int, input().split())
visited = [[0] * M for _ in range(N)] # 방문한 위치를 저장하는 visited

X, Y, direction = map(int, input().split()) # 현재 좌표 X, Y, 보고있는 방향

# 바다와 갈 수 없는 곳의 정보를 갖고 있는 array list
array = []
for i in range(N):
    array.append(list(map(int, input().split())))

# 북 동 남 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# turn left
def turnLeft():
    # block 바깥의 변수를 글로벌을 통해 가져옴
    global direction
    # 북 -> 서 -> 남 -> 동 순서대로 움직임
    direction -= 1
    if direction == -1:
        direction = 3

# Start simulation
count = 0 # 방문한 횟수
turnTime = 0 # 움직임 횟수

while True:
    # 왼쪽으로 회전
    turnLeft()
    # 회전된 direction 값을 가지고
    # 다음에 이동할 곳의 좌표를 (nX, nY)에 담는다
    nX = X + dx[direction]
    nY = Y + dy[direction]
    # 회전한 이후 가보지 않은 칸이나 바다인 경우
    if visited[nX][nY] == 0 and array[nX][nY] == 0:
        # 해당 칸을 방문했다는 표시를 남기고
        visited[nX][nY] = 1
        # 위치를 그곳으로 옮긴다. 여기서 중요한 부분은 array 즉 입력하는 board의 값은 변하지 않는다.
        X = nX
        Y = nY
        count += 1
        turnTime = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우, visited[nX][nY] != 0 and array[nX][nY] != 0
    else:
        turnTime += 1

    # 네 방향 모두 갈 수 없는 경우
    if turnTime == 4:
        nX = X - dx[direction]
        nY = Y - dy[direction]

        # 뒤로 갈 수 있다면
        if array[nX][nY] == 0:
            X = nX
            Y = nY

        # 뒤에 바다로 막혀있을 경우, array[nX][nY] == 1
        else:
            break
        # 갈 곳이 있다면 도는 행위 초기화
        turnTime = 0

print(count)
