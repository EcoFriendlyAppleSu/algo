'''
문제 : 치킨 배달
'''

'''
나의 풀이 - 뭐가 틀린지 보이지 않는다.

def distance(house, chickenHouse):
    x1, y1 = house
    x2, y2 = chickenHouse
    return abs(x1 - x2) + abs(y1 - y2)


def generateChickenAndHouseList(board, n):
    chickens = []
    houses = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                chickens.append((i, j))
            elif board[i][j] == 1:
                houses.append((i, j))
    return chickens, houses


def solution():
    n, m = map(int, input().split())
    answer = []
    board = [list(map(int, input().split())) for _ in range(n)]  # board init
    chickenList, houseList = generateChickenAndHouseList(board, n)  # 치킨집, 집 위치 리스트
    pickUpMSizeChicken = list(combinations(chickenList, m))

    for positions in pickUpMSizeChicken:  # ((1, 2), (2, 2), (4, 4)) m개 뽑은 상황에서 최소값
        result = 0
        for position in positions:  # (1, 2), (2, 2), (4, 4)
            temp = INF
            for house in houseList:  # 집의 좌표
                temp = min(temp, distance(house, position))
            result += temp
        answer.append(result)
    return min(answer)


if __name__ == '__main__':
    print(solution())

'''
from itertools import combinations

INF = int(1e9)
n, m = map(int, input().split())
chicken, house = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i,j))
        elif data[j] == 2:
            chicken.append((i,j))

candidates = list(combinations(chicken, m))

def getSum(candidate):
    result = 0
    for hx, hy in house:
        temp = INF
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = INF
for candidate in candidates:
    result = min(result, getSum(candidate))
print(result)

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2