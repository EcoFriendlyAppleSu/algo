# 소수 구하기
from itertools import combinations
import math

def judgePrimeNumber(num):

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    result = []
    tempAry = []
    nums = list(combinations(nums, 3))
    for i in nums:
        tempAry.append(sum(i))
    for i in tempAry:
        if judgePrimeNumber(i) == True:
            result.append(i)
        else:
            continue
    return len(result)


if __name__ == '__main__':
    nums = [1,2,7,6,4]
    print(solution(nums))


# def solution(ary):
#     result = []
#     count = 0
#     for x in range(0, len(ary)-2):
#         for y in range(x+1,len(ary)-1):
#             for z in range(y+1,len(ary)):
#                 result.append(ary[x]+ary[y]+ary[z])
#
#     for x in result:
#         boolean = True
#         for y in range(2,x):
#             if x % y == 0:
#                 boolean = False
#                 break
#         if boolean is True:
#             print(x)
#             count += 1
#     return count

