# flag Or else
# python에선 for else를 사용할 수 있다.
import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')


# import operator
# from itertools import accumulate
# def solution(input):
#     flag = False
#     values = list(accumulate([2, 4, 2, 5, 1], operator.mul))
#     for i in input:
#         if (i ** 2) in values:
#             flag = True
#         else:
#             continue
#
#         if flag == True:
#             break
#     if flag == False:
#         return "not found"
#     else:
#         return "found"