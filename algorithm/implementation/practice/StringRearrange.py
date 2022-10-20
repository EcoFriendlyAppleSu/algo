# 문자열 재정렬

string = "K1KA5CB7"
stringList = list(string)
stringList.sort()
result = []
number = 0
for i in stringList:
    if i.isdigit():
        number += int(i)
    else:
        result.append(i)

result.append(str(number))
print("".join(result))

