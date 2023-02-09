'''
백준 문제 : 내일 할거야
조건을 보고 알맞는 자료구조를 선택해야합니다.
'''
import sys

n = int(sys.stdin.readline())
works = []
temp = 0
for _ in range(n):
    d, t = list(map(int, sys.stdin.readline().split()))
    works.append((d,t))
    if t > temp:
        temp = t
print(works)

works.sort(key= lambda x:x[1], reverse=True)
print(works) # [(1, 13), (3, 10), (2, 8)]

for work in works:
    currentD, currentT = work
    if currentT < temp:
        temp = currentT
    temp -= currentD
print(temp)

'''
3
2 8
1 13
3 10
'''