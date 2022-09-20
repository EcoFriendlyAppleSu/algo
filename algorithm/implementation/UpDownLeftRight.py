# 상하좌우

# my solution
# R = [0,1]
# U = [-1,0]
# L = [0,-1]
# D = [1,0]
# N = int(input())
# def movePosition(pos, move):
#     if move == 'R':
#         movePos = R
#     elif move == 'U':
#         movePos = U
#     elif move == 'L':
#         movePos = L
#     else:
#         movePos = D
#
#     tempPos = [pos[0] + movePos[0], pos[1] + movePos[1]]
#     if tempPos[0] <= 0 or tempPos[0] > N or tempPos[1] <= 0 or tempPos[1] > N:
#         return pos
#     else:
#         return tempPos
#
#
# def solution():
#     MoveList = list(map(str, input().split()))
#     position = [1,1]
#
#     for Move in MoveList:
#         position = movePosition(position, Move) # 이렇게 호출할 수 있다는 것을 기억하자
#     return position
#
# if __name__ == '__main__':
#     print(solution())

N = int(input())
x, y = 1,1
plans = input().split()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
moveType = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(moveType)):
        if plan == moveType[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny
print(x,y)
