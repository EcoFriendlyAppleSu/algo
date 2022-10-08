# 떡볶이 떡 만들기

N, M = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array) # 최대값 구하고

while(start <= end):
    total = 0
    mid = (start + end) // 2

    # 떡의 양을 계산하는 for loop
    for x in array:
        if x > mid:
            total += x - mid

    # 자른 떡의 양보다 손님이 원하는 떡의 양이 더 클경우 (왼쪽 부분 탐색)
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)