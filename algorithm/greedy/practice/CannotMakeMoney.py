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

# 다른 답안
# target이 되는 수 아래에 있는 숫자들은 당연히 만들 수 있다는게 확실하다.
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)

# 5
# 3 2 1 1 9