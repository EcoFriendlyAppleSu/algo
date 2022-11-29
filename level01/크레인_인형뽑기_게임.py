def solution(board, moves):
    answer = 0
    stack = []
    board = [[row[i] for row in board[::-1]] for i in range(len(board[0]))]
    print(board)
    for i in moves:
        i = i - 1  # board size 맞추는 라인
        temp = 0

        for j in range(len(board[i]) - 1, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0
                break

        if temp == 0:
            continue

        if len(stack) == 0:
            stack.append(temp)
            continue
        else:
            popStack = stack.pop()
            if popStack == temp:
                answer += 1
                continue
            else:
                stack.append(popStack)
                stack.append(temp)
                continue

    return print(answer * 2)


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

solution(board, moves)
