'''
https://www.acmicpc.net/problem/2798
'''

from itertools import combinations


def get_combination(ary, n):
    result = []

    if n == 0:
        return [[]]
    if n == 1:
        result = [[i] for i in ary]
        return result
    for i in range(len(ary)):
        element = ary[i]
        c = combinations(ary[i + 1:], n - 1)
        for each_result in c: # 기본적으로 tuple로 반환됩니다.
            result.append([element] + list(each_result))
    return result

def add_value_with_not_over_m(each_list, m):
    if sum(each_list) <= m:
        return sum(each_list)
    return 0


n, m = map(int, input().split())
# numbers = set(list(map(int, input().split())))
numbers = list(map(int, input().split()))
# numbers_list = list(combinations(numbers, 3))
numbers_list = get_combination(numbers, 3)

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
