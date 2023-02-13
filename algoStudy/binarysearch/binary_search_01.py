'''
백준 문제 : 1920
'''

import sys

N = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))


def binarySerch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return False

def binarySerchUsingRecurisve(array, target, start, end):

    # Recursive exit condition
    if start > end:
        return False
    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binarySerchUsingRecurisve(array, target, start, mid -1)
    elif array[mid] < target:
        return binarySerchUsingRecurisve(array, target, mid + 1, end)


nList.sort()
print(nList) # [1, 2, 3, 4, 5]

print(mList) # [1, 3, 7, 9, 5]

for target in mList:
    # result = binarySerch(nList, target, 0, len(nList) - 1)
    result = binarySerchUsingRecurisve(nList, target, 0, len(nList) - 1)
    if result is True:
        print(1)
    else:
        print(0)

'''
5
4 1 5 2 3
5
1 3 7 9 5
'''
