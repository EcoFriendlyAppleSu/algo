'''
백준 문제 : 2110
 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)
 공유기를 설치할 거리를 이분 탐색으로 결정해야 합니다.
'''
import sys
n, c = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(n)]

houses.sort()

result = 0
left = 1
right = houses[-1] - houses[0]

if c == 2: # 집이 2개라면 처음과 마지막 집에 공유기를 설치해야 최대 값이 됩니다.
    print(houses[- 1] - houses[0])
else:
    while left < right:
        mid = (left + right) // 2

        count = 1
        standardHouse = houses[0]

        for i in range(n):
            if houses[i] - standardHouse >= mid:
                count += 1
                standardHouse = houses[i]

        if count >= c:
            result = mid
            left = mid + 1
        elif count < c:
            end = mid
    print(result)
# while left <= right:
#
#     if (houses[left + 1] - houses[left]) - 1 >= 0 and (houses[right] - houses[right - 1]) - 1 >= 0:
#         if distance < (houses[left + 1] - houses[left] - 1):
#             distance = houses[left + 1] - houses[left] - 1
#         left += 1
#
#         if distance < (houses[right] - houses[right - 1] - 1):
#             distance = houses[right] - houses[right - 1] - 1
#         right -= 1



'''
5 3
1
2
8
4
9
'''