# 이진 탐색

# 재귀 사용

# param = 배열, 찾고자하는 숫자, 시작점, 끝점
def binarySearch(array, target, start, end):
    # 시작점이 끝점보다 위치값이 크다면
    if start > end:
        return None
    mid = (start + end) // 2 # 중간 값을 구합니다. 수가 홀수라면 내림을 사용

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binarySearch(array, target, mid+1, end) # target은 살필 필요가 없으니 start poition is mid index plus 1
    elif array[mid] > target:
        return binarySearch(array, target, start, mid-1) # end position is mid index minus 1

N, target = map(int, input().split())
array = list(map(int, input().split()))


result = binarySearch(array, target, 0, N-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

# 10 7
# 1 3 5 7 9 11 13 15 17 19
