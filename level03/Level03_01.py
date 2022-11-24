'''
문제 : 파괴되지 않는 건물
'''


def solution(board, skill):
    answer = 0
    temp = [[0 for j in range(len(board[0]))] for _ in range(len(board))]
    print(temp)

    for i in range(len(skill)):
        durabiliity = skill[i][0]
        x1, y1 = skill[i][1], skill[i][2]
        x2, y2 = skill[i][3], skill[i][4]
        if durabiliity == 1:
            value = skill[i][5] * (-1)
        else:
            value = skill[i][5]

        for moveX in range(x1, x2 + 1):
            for moveY in range(y1, y2 + 1):
                board[moveX][moveY] += value
                if i == len(skill) and board[moveX][moveX] > 0:
                    answer += 1

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer += 1

    return answer


def prefixSum(board, skill):
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    # 누적합 세팅
    for type, x1, y1, x2, y2, degree in skill:
        temp[x1][y1] += degree if type == 2 else -degree
        temp[x1][y2 + 1] += -degree if type == 2 else degree
        temp[x2 + 1][y1] += -degree if type == 2 else degree
        temp[x2 + 1][y2 + 1] += degree if type == 2 else -degree

    # 각 합을 더해주면서 개별 index당 내구성 가중치를 계산
    for i in range(len(temp) - 1):
        for j in range(len(temp[0]) - 1):
            temp[i][j + 1] += temp[i][j]

    for j in range(len(temp[0]) - 1):
        for i in range(len(temp) - 1):
            temp[i + 1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0: answer += 1
    print(answer)


if __name__ == '__main__':
    print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
                   [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
    print(prefixSum([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
                    [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
