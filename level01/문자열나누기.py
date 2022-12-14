def solution(s):
    answer = 0
    temp = []
    index = 0
    while index < len(s):
        current = s[index]
        if len(temp) == 0:
            temp.append(current)
            index += 1
            continue
        else:
            if temp[0] == current:
                temp.append(current)
                index += 1
                continue
            else:
                temp.append(current)
                if temp.count(temp[0]) == (len(temp)-temp.count(temp[0])):
                    answer += 1
                    temp = []
                    index += 1
                else:
                    index += 1
    if len(temp) != 0:
        answer += 1

    return answer


print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))

'''
    answer = 0
    result = []
    index = 0
    temp = []
    while index < len(s):
        currentValue = s[index]
        if len(temp) == 0:
            temp.append(currentValue)
            index += 1
            continue
        if currentValue in temp:
            temp.append(currentValue)
            index += 1
        else:
            temp.append(currentValue)
            result.append("".join(temp))
            temp = []
            index += 1
    if len(temp) != 0:
        result.extend(temp)
    print(result)
'''
