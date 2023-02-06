'''
백준 문제 : 수 정렬하기 3
메모리 초과
'''
import sys

n = int(sys.stdin.readline())
li = [0] * (n+1)

for i in range(n):
    inputNumber = int(sys.stdin.readline())
    li[inputNumber] += 1

index = 0
while True:
    if index == n:
        break
    if li[index] == 0:
        index += 1
        continue
    if li[index] != 0:
        print(index)
        li[index] -= 1

'''
import sys

N = int(input())

check_list = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())
    
    check_list[input_num] = check_list[input_num] + 1
    
for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)
'''

'''
10
5
2
3
1
4
2
3
5
1
7
'''