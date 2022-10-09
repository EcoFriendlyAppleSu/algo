# 1로 만들기
# Bottom Up

x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
# 횟수를 담고 있는 board
board = [0] * 100

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우, 횟수 추가
    board[i] = board[i-1] + 1

    # min 함수에서 비교를 통해 최소 값을 구하는 과정을 거칠거야
    # 1을 빼고 횟수를 하나 추가한 것과 2 or 3 or 5 로 나눌 수 있는 경우에서
    # 어떤 것이 최소 값을 갖는지 판단하는 분기 로직
    if i % 2 == 0:
        board[i] = min(board[i], board[i // 2] + 1)
    if i % 3 == 0:
        board[i] = min(board[i], board[i // 3] + 1)
    if i % 5 == 0:
        board[i] = min(board[i], board[i // 5] + 1)

for i in range(len(board)):
    print(i, "번 index입니다. ", board[i])
