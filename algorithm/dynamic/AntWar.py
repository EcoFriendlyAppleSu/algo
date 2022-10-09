# 개미 전쟁

N = int(input())
array = list(map(int, input().split()))

# 최대 값의 가중치를 담는 board
board = [0] * 100

board[0] = array[0]
board[1] = max(array[0], array[1])

for i in range(2, N):
    board[i] = max(board[i-1], board[i-2] + array[i])

print(board[N-1])