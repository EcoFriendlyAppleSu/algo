'''
https://www.acmicpc.net/problem/10819 문제
'''
from itertools import permutations


def get_sum_each_ary(each_ary): # 주어진 길이 n-1 번의 반복을 수행해 값을 더합니다.
    temp_result = 0
    for i in range(len(each_ary) - 1):
        temp_result += abs(each_ary[i] - each_ary[i+1])
    return temp_result

n = int(input())  # n개 정수 입력
ary = list(map(int, input().split()))  # 정수 입력

temp_ary = list(permutations(ary, n)) # 순열을 통해 모든 경우의 수를 구합니다.
result = [] # 결과를 담을 list

for each_ary in temp_ary:
    result.append(get_sum_each_ary(each_ary))

print(max(result))

'''
6
20 1 15 8 4 10
'''
