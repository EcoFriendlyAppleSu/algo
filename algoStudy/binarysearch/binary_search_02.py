'''
백준 문제 : 2805
'''
import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def binarySearch(trees, start, end, target):

    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for tree in trees:
            if (tree - mid) < 0:
                continue
            temp += (tree - mid)
        if temp >= target:
            start = mid + 1
        elif temp < target:
            end = mid - 1
    return end


result = binarySearch(trees, 0, max(trees), m)
print(result)
'''
4 7
20 15 10 17
'''