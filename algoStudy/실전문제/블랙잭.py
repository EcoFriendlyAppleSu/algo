'''
https://www.acmicpc.net/problem/2798
'''

from itertools import combinations

def add_value_with_not_over_m(each_list, m):
    if sum(each_list) <= m:
        return sum(each_list)
    return 0
n, m = map(int, input().split())
numbers = set(list(map(int, input().split())))
numbers_list = list(combinations(numbers, 3))

result = []

for each_numbers in numbers_list:
    result.append(add_value_with_not_over_m(each_numbers, m))

print(max(result))

'''
5 21
5 6 7 8 9

10 500
93 181 245 214 315 36 185 138 216 295
'''