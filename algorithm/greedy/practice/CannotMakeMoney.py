# 만들 수 없는 금액
from itertools import combinations

amountOfCoin = int(input())
coins = list(map(int, input().split()))
result = [0] * (sum(coins)+1)
index = 0

for i in coins:
    result[i] += 1

for i in range(2, len(coins)):
    temp = set(combinations(coins, i))
    for j in temp:
        result[sum(j)] += 1

for i in range(1, len(result)):
    if result[i] == 0:
        index = i
        break
print(index)

# 5
# 3 2 1 1 9