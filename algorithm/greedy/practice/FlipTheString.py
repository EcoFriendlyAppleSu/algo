# 문자열 뒤집기
# 연속된 하나 이상의 수를 뒤집을 수 있습니다.

string = input()
stringList = list(map(int, string))

countZero = 0
countOne = 0

if stringList[0] == 1:
    countZero += 1
else:
    countOne += 1

for i in range(len(stringList) -1):
    if stringList[i] != stringList[i+1]:
        if stringList[i+1] == 1:
            countZero += 1
        else:
            countOne += 1

print(min(countOne, countZero))

# 0001100