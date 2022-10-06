# 선택 정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    minValue = i

    # 최소 값만 비교하는 loop
    for j in range(i+1, len(array)):
        if array[minValue] > array[j]:
            minValue = j
    array[i], array[minValue] = array[minValue], array[i]

print(array)