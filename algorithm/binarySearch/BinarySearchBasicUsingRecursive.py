# 이진 탐색

# 재귀 사용

# param = 배열, 찾고자하는 숫자, 시작점, 끝점
def binarySearch(array, target, start, end):
    # 시작점이 끝점보다 위치값이 크다면 즉 정렬이 안되어 있다는 말과 동일
    if start > end:
        return None

    # 중간 값을 구합니다. 수가 홀수라면 내림을 사용
    mid = (start + end) // 2

    # 배열의 중간 값이 찾고자하는 값과 같다면
    if array[mid] == target:
        # 해당 배열 index값을 반환
        return mid
    elif array[mid] < target: # target은 살필 필요가 없으니 start poition is mid index plus 1
        return binarySearch(array, target, mid +1, end)

    elif array[mid] > target: # end position is mid index minus 1
        return binarySearch(array, target, start, mid -1)

N, target = map(int, input().split())
array = list(map(int, input().split()))


result = binarySearch(array, target, 0, N-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

# 10 7
# 1 3 5 7 9 11 13 15 17 19
