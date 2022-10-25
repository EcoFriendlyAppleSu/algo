'''
문제 기둥과 보 설치
요소를 크게 가져가는 방법을 생각해보자
'''


# def solution(buildFrame):
#     # board 만들 시 최대 값을 구해야 합니다.
#     maxRow = 0
#     for i in buildFrame:
#         if i[0] > maxRow:
#             maxRow = i[0]
#
#     # 건물을 나타내는 board
#     board = [[0] * (maxRow) for _ in range(maxRow * 2)]
#     print(buildFrame)
#     for frame in buildFrame:
#         # x 좌표, y 좌표, 기둥(0) 혹은 보(1), 삭제(0) 혹은 설치(1)
#         x, y, component, install = frame
#
#         # 기둥일 경우
#         if component == 0:
#             # 바닥면에서 시작했을 때
#             if y == 0:
#                 print(x,y)
#                 board[x][y] += 1  # 바닥면 좌표 +1
#                 board[x][y + 1] += 1  # 기둥 세운 후 좌표 +1
#                 continue
#             # 보의 한쪽 끝 부분이거나 다른 기둥 위에 있을 경우
#             if board[x][y] == 1:
#                 board[x][y + 1] += 1  # 기둥을 세운 후 끝점인 곳에 +1
#         # 보일 경우
#         elif component == 1:
#             # 시작하는 지점이 보의 끝일 경우
#             if board[x][y] == 1:
#                 # 다음 보 연결
#                 board[x+1][y] += 1
#             # 시작하는 지점이 0일 경우
#             elif board[x][y] == 0:
#                 # 다음 지점이 기둥의 끝 혹은 보일 때
#                 if board[x+1][y] == 1:
#                     board[x][y] += 1
#
#     print(board)
#     return None

def possible(answer):
    for x, y, component in answer:
        if component == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif component == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
        return True


def solution(buildFrame):
    answer = []

    for frame in buildFrame:
        x, y, component, operate = frame
        if operate == 0:
            answer.remove([x, y, component])
            if not possible(answer):
                answer.append([x, y, component])

        if operate == 1:
            answer.append([x, y, component])
            if not possible(answer):
                answer.remove([x, y, component])
    return sorted(answer)


if __name__ == '__main__':
    buildFrame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
                  [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
    print(solution(buildFrame))
