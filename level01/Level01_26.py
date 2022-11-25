'''
문제 : 다트 게임
'''


def solution(dartresult):
    answer = 0
    result = []
    dartresult = dartresult.replace('10', 'F')
    dartresult = list(dartresult)

    temp_int = 0
    for x in range(len(dartresult)):
        if dartresult[x].isdigit() == True:
            temp_int = int(dartresult[x])

        elif dartresult[x].isdigit() == False:
            if dartresult[x] == 'F':
                temp_int = 10
            if dartresult[x] == 'S' or dartresult[x] == 'D' or dartresult[x] == 'T':
                if dartresult[x] == 'S':
                    temp_1 = temp_int ** 1
                    result.append(temp_1)
                elif dartresult[x] == 'D':
                    temp_2 = temp_int ** 2
                    result.append(temp_2)
                elif dartresult[x] == 'T':
                    temp_3 = temp_int ** 3
                    result.append(temp_3)
            if dartresult[x] == '#' or dartresult[x] == '*':
                result.append(dartresult[x])

    for x in range(len(result)):
        if result[x] == '#':
            result[x - 1] *= (-1)
        elif result[x] == '*':
            if x == 1:
                result[0] *= 2
            else:
                result[x - 1] *= 2
                if result[x - 2] == '#' or result[x - 2] == '*':
                    result[x - 3] *= 2
                else:
                    result[x - 2] *= 2

    for x in range(len(result)):
        if result[x] == '#' or result[x] == '*':
            continue
        answer += result[x]

    return answer


if __name__ == '__main__':
    print(solution("1S2D*3T"))
