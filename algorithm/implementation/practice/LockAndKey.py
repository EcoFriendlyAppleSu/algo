'''
자물쇠와 열쇠
리스트를 돌리는 과정을 꼭 기억하고 넘어가자
key = [[row[i] for row in key[::-1]] for i in range(len(key[0]))]
'''


def checkBoard(board):
    lockLength = len(board) // 3
    for i in range(lockLength, lockLength * 2):
        for j in range(lockLength, lockLength * 2):
            if board[i][j] != 1:
                return False
    return True


def solution(lock, key):
    lockLength = len(lock)
    keyLength = len(key)
    boardSize = lockLength * 3
    # board init
    board = [[0] * boardSize for _ in range(boardSize)]
    print(board)

    # board setting
    for i in range(lockLength):
        for j in range(lockLength):
            board[i+lockLength][j+lockLength] = lock[i][j]

    print(board)

    # key board 비교
    for _ in range(4):
        key = [[row[i] for row in key[::-1]] for i in range(len(key[0]))]
        for x in range(lockLength * 2):
            for y in range(lockLength * 2):
                # 자물쇠 끼우기
                for i in range(keyLength):
                    for j in range(keyLength):
                        board[x+i][y+j] += key[i][j]
                if checkBoard(board) == True:
                    return True
                # 자물쇠 빼기
                for i in range(keyLength):
                    for j in range(keyLength):
                        board[x+i][y+j] -= key[i][j]


if __name__ == '__main__':
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(lock, key))
