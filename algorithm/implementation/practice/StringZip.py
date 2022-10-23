'''
문제 : 문자열 압축
생각해야 할 부분
문제의 시작점을 항상 잘 유지하다.
'''

# string = "aabbaccc"
# result = [] # 결과를 담는 result
# stringList = list(string)
# print(stringList)
#
# canDivideList = []
# for i in range(1, len(string)):
#     if len(string) % i == 0:
#         canDivideList.append(i)
#
# print(canDivideList)
#
# for zipSize in canDivideList: # 1 2 4
#     temp = 0
#     tempString = string[:zipSize]
#     check = 1
#     resultString = ""
#     for i in range(len(string) // zipSize):
#         if stringList[temp:temp+zipSize] == stringList[temp+zipSize : temp + (zipSize * 2)]:
#             temp += zipSize
#             check += 1
#         else:
#             resultString += str(check) + string[temp:temp+zipSize]
#             check = 0
#             continue
#     if check != 0:
#         resultString += str(check) + string[temp:temp+zipSize]
#     print(resultString)

def solution(string):
    result = []

    if len(string) == 1:
        return 1

    # 시작부터 반복하는 문자열의 수를 카운트 하는 loop
    for i in range(1, (len(string) // 2) + 1):
        tempResult = ''
        count = 1
        tempString = string[:i]
        # 자른 길이만큼 반복되는 loop
        for j in range(i, len(string), i):
            if tempString == string[j:j+i]:
                count += 1
            elif tempString != string[j:j+i]:
                if count != 1:
                    # 기존의 result + 새로 반복되는 문자열
                    tempResult = tempResult + str(count) + tempString
                else:
                    tempResult = tempResult + tempString
                tempString = string[j:j+i]
                count = 1
        if count != 1:
            tempResult = tempResult + str(count) + tempString
        else:
            tempResult = tempResult + tempString
        result.append(len(tempResult))
    return min(result)
if __name__ == '__main__':
    string = "aabbaccc"
    print(solution(string))