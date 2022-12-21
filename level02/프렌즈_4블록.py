'''
SET 사용을 머리 속에 담아 두자
'''
def solution(m, n, board):
    answer = 0
    # 매 번마다 복사해 사용할 삭제 판단 보드 True : 삭제, False : 삭제 아님
    # tempBoard = [[False] * n for _ in range(m)]
    board = [list(board[i]) for i in range(len(board))]

    # 900 % 4 = 225 O( 255 * ( 900 + 900 + 30 + 900 ))
    while True:
        temp = 0
        TFBoard = [[False] * n for _ in range(m)]

        # 4 개의 공간 체크
        # 30 * 30 = 900
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != " ":
                    if board[i][j] is board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == \
                            board[i + 1][j + 1]:
                        TFBoard[i][j] = True
                        TFBoard[i][j + 1] = True
                        TFBoard[i + 1][j] = True
                        TFBoard[i + 1][j + 1] = True

        # 30 * 30 = 900
        for i in range(m):
            for j in range(n):
                if TFBoard[i][j] == True:
                    board[i][j] = " "
        # 공간 Count
        # 30
        for index in TFBoard:
            temp += index.count(True)

        # infinity loop(while) escape condition
        if temp == 0:
            break
        else:
            answer += temp

        # board를 당기는 작업
        while True:
            moved = 0
            # 30 * 30 = 900
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] != " " and board[i + 1][j] == " ":
                        board[i + 1][j] = board[i][j]
                        board[i][j] = " "
                        moved = 1
            if moved == 0:
                break
    return answer


def solution2(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    cnt = 0
    rm = set()
    while True:
        # 보드를 순회하며 4블록이 된 곳의 좌표를 집합에 기록
        for i in range(m - 1):
            for j in range(n - 1):
                t = board[i][j]
                if t == []:
                    continue
                if board[i + 1][j] == t and board[i][j + 1] == t and board[i + 1][j + 1] == t:
                    rm.add((i, j));
                    rm.add((i + 1, j))
                    rm.add((i, j + 1));
                    rm.add((i + 1, j + 1))

        # 좌표가 존재한다면 집합의 길이만큼 세주고 블록을 지움
        if rm:
            cnt += len(rm)
            for i, j in rm:
                board[i][j] = []
            rm = set()
        # 없다면 함수 종료
        else:
            return cnt

        # 블록을 위에서 아래로 당겨줌
        while True:
            moved = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] != [] and board[i + 1][j] == []:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break

# print(solution2(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
