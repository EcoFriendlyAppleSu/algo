# 행렬 테두리 회전하기
# 덮어 씌우면 된다. 잘하자

def rotate(pointers, board):
    # (x1, y1, x2, y2)
    pointers = [x-1 for x in pointers]
    x1, y1, x2, y2 = pointers
    temp = board[x1][y1]
    minValue = temp

    # 좌측 열
    for k in range(x1+1, x2+1):
        board[k-1][y1] = board[k][y1]
        minValue = min(minValue, board[k][y1])

    # 아래 행
    for k in range(y1+1, y2+1):
        board[x2][k-1] = board[x2][k]
        minValue = min(minValue, board[x2][k])

    # 우측 열
    for k in range(x2-1, x1-1, -1):
        board[k+1][y2] = board[k][y2]
        minValue = min(minValue, board[k][y2])

    # 상단 행
    for k in range(y2-1, y1-1, -1):
        board[x1][k+1] = board[x1][k]
        minValue = min(minValue, board[x1][k])
    board[x1][y1+1] = temp
    return board, minValue

def solution(row, col, queries):
    answer = []
    # board = [[0 for i in range(col + 1)] for j in range(row + 1)]
    board = []
    for i in range(row):
        board.append([a for a in range(i*col+1, (i+1)*col+1)])

    print(board)
    for q in queries:
        board, Min = rotate(q, board)
        answer.append(Min)
    print(answer)


if __name__ == '__main__':
    row = 6
    col = 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    solution(row, col, queries)