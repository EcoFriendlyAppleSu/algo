# 효율적인 화폐 구성

N, M = map(int, input().split())

currencies = []
for i in range(N):
    currencies.append(int(input()))

board = [10001] * (M +1)

board[0] = 0

for i in range(N):
    for j in range(currencies[i], M + 1):
        if board[j - currencies[i]] != 10001:
            board[j] = min(board[j], board[j - currencies[i]] + 1)
if board[M] == 10001:
    print(-1)
else:
    print(board[M])


# input
# 2 15
# 2
# 3