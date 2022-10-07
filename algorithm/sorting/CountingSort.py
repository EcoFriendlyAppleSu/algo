# 계수 정렬
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 계수 정렬에 필요한 숫자를 담을 수 있는 array index == targetNumber
countArray = [0] * (max(array) + 1)

for i in range(len(array)):
    countArray[array[i]] += 1

print(countArray)

for i in range(len(countArray)): # index looping
    for j in range(countArray[i]): # 횟수 looping
        print(i , end= ' ')
print()
# Using sorted method
usingSortedMethod = sorted(array)
print(usingSortedMethod)

# Using sort() method in intList
array.sort()
print(array)

# Sorting Using Key
array = [('banana', 2), ('apple', 5), ('waterMelon', 3)]
def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
