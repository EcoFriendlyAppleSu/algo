import itertools
from functools import reduce

# def solution(mylist):
#     answer = []
#     for i in mylist:
#         for j in i:
#             answer.append(j)
#
#     return answer
#
# if __name__ == '__main__':
#     mylist = [['A', 'B'], ['X', 'Y'], ['1']]
#     print(solution(mylist))

# 곱집합(Cartesian product) using itertools
# iterable1 = 'ABCD'
# iterable2 = 'xy'
# iterable3 = '1234'
# print(list(itertools.product(iterable1, iterable2, iterable3)))
# print(list(zip(iterable1, iterable2, iterable3))) # 가장 작은 길이의 list에 맞춰 zip을 출력한다.

# 2D list를 1D로 만들기
my_list = [[1, 2], [3, 4], [5, 6]]

# print(sum(my_list, []))
# print(list(itertools.chain.from_iterable(my_list)))
print(list(itertools.chain(*my_list)))
# print(list(reduce(lambda x, y: x+y, my_list)))
