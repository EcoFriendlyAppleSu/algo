# 이상한 문자 만들기

def solution(string):
    answer = string.split()
    temp = []
    result = []
    for i in answer:
        for j in range(len(i)):
            if (j % 2) == 0:
                temp.append(i[j].upper())
            else:
                temp.append(i[j].lower())

    temp = "".join(temp)
    temp = temp[:len(temp)]

    index = 0
    for i in string:
        if i != ' ':
            result.append(temp[index])
            index += 1
        if i == ' ':
            result.append(' ')
    result = "".join(result)
    return result


if __name__ == '__main__':
    string = "try hello world"
    print(solution(string))