# 퀵 정렬
array = [5,7,9,0,3,1,6,2,4,8]

# parameter 변수로 올 수 있는 것들은 변화하는 것들이다.
def quickSort(array, start, end):
    if start >= end: # 원소가 한개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 크고 end 보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quickSort(array, start, right-1)
    quickSort(array,right+1, end)

quickSort(array,0,len(array)-1)
print(array)