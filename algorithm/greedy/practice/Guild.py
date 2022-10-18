# 모험가 길드

n = int(input())
fears = list(map(int, input().split()))
count = 0
result = 0
while n > 0:
    count = 0
    X = n
    for i in fears:
        if i == X:
            count += 1
    if X <= count:
        result += 1
    n -= 1
print(result)