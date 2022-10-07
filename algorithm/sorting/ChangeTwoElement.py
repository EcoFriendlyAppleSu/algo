# 두 배열의 원소 교체

N, M = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

print(aList)
print(bList)

aList.sort()
bList.sort(reverse=True)

print(aList)
print(bList)

for i in range(M):
    aList[i], bList[i] = bList[i], aList[i]

print(sum(aList))