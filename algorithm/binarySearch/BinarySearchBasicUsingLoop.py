# 이진 탐색

# 반복문을 사용한 이진 트리

def binarySearch(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        # 찾는 값이 배열 중간 값보다 작다면
        elif array[mid] > target:
            end = mid -1
        elif array[mid] < target:
            start = mid + 1
    return None


N, target = map(int, input().split())
array = list(map(int, input().split()))


result = binarySearch(array, target, 0, N-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

# input values
# 10 7
# 1 3 5 7 9 11 13 15 17 19
