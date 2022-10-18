# 곱셈 혹은 더하기
number = input()
numberList = list(map(int, number))
print(numberList)

result = 1

for index in numberList:
    if index == 0:
        continue
    else:
        result *= index

print(result)