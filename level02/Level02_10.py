# 거리두기 확인하기

from collections import deque

BOARD_RANGE = 5
def solution(places):

    answer = []

    for place in places:

        key = False # 거리두기 체크 변수
        currentAry = [] # 현재 있는 방

        for current in place: # return "POOOP" to ["P","O","O","O","P"]
            currentAry.append(list(current))

        for i in range(BOARD_RANGE):
            if key:
                break
            for j in range(BOARD_RANGE):
                if key:
                    break

                if currentAry[i][j] == "P":
                    if (i + 1) < BOARD_RANGE:
                        if currentAry[i+1][j] == "P":
                            key = True
                            break
                        if  currentAry[i+1][j] == "O":
                            if (i + 2) < BOARD_RANGE:
                                if currentAry[i+2][j] == "P":
                                    key = True
                                    break

                    if (j + 1) < BOARD_RANGE:
                        if currentAry[i][j+1] == "P":
                            key = True
                            break
                        if currentAry[i][j + 1] == "O":
                            if (j + 2)< BOARD_RANGE:
                                if currentAry[i][j+2] == "P":
                                    key = True
                                    break

                    if (i + 1) < BOARD_RANGE and (j + 1) < BOARD_RANGE:
                        if currentAry[i + 1][j + 1] == "P" and (
                                currentAry[i + 1][j] == "O" or currentAry[i][j + 1] == "O"):
                            key = True
                            break
                    if (i + 1) < BOARD_RANGE and (j - 1) >= 0:
                        if currentAry[i + 1][j - 1] == "P" and (currentAry[i + 1][j] == "O" or currentAry[i][j - 1] == "O"):
                            key = True
                            break
        if key:
            answer.append(0)
        else:
            answer.append(1)
    return answer


def bfs(p, idx):
    q = deque([idx])
    visited = [[False] * 5 for _ in range(5)]
    dic = {0: [0, -1], 1: [-1, 0], 2: [0, 1], 3: [1, 0]}

    while q:
        x, y, d = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]
            nd = d + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True

                if p[nx][ny] == 'P': # 다음으로 옮긴 곳이 P라면 거리두기를 지키지 않은 것
                    if nd <= 2:
                        return False

                elif p[nx][ny] == 'O':
                    if nd == 1:
                        q.append([nx, ny, nd])

    return True


def solutionUsingBFS(places):
    answer = []

    for p in places:
        flag = 1 # 거리두기를 지는지 판단하는 flag. 지킨다면 return 1, 아니라면 return 0

        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    result = bfs(p, [i, j, 0])
                    if not result:
                        flag = 0

        answer.append(flag)

    return answer
if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solutionUsingBFS(places))