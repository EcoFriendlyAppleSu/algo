# 볼링공 고르기
# from itertools import combinations
#
# n, m = map(int, input().split())
# ballWeight = list(map(int, input().split()))
# result = 0
#
# ballNumber = [i for i in range(n)]
# print(ballNumber)
# combinList = list(combinations(ballNumber, 2))
#
# for i in combinList:
#     x, y = i
#     if ballWeight[x] == ballWeight[y]:
#         continue
#     result += 1
# print(result)

n, m = map(int, input().split())
data = list(map(int, input().split()))
array = [0] * 11

for x in data:
    array[x] += 1

result = 0

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

# 5 3
# 1 3 2 3 2

# 8 5
# 1 5 4 3 2 4 5 2