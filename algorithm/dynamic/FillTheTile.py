# 타일 채우기

N = int(input())

board = [0] * 101

board[1] = 1
board[2] = 3 # board[1] + 2 가지 방법

for i in range(3, N+1):
    board[i] = (board[i-1] + board[i - 2] * 2) %796796

print(board[N])
