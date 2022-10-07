# 위에서 아래로
time = int(input())
board = []
for i in range(time):
    board.append(int(input()))

result = sorted(board, reverse=True)

print(result)
