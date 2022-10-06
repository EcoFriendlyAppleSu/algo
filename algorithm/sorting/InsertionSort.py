# 삽입 정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else: # 오름 차순에서 우측에 있는 데이터가 죄측에 있는 데이터보다 크다면 break
            break
print(array)