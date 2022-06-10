# 문자열 압축

def solution(string):
    result = []

    if len(string) == 1:
        return 1

    for i in range(1, (len(string)//2)+1):
        tempResult = ''
        count = 1
        tempString = string[:i]

        for j in range(i, len(string), i): # i 부터 len(string)만큼 i 만큼 잘라서
            if tempString == string[j:i+j]:
                count += 1
            else:
                if count != 1:
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
    print(result)
    return min(result)


if __name__ == '__main__':
    string = "aabbaccc"
    print(solution(string))