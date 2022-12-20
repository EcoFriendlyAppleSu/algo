'''
문자열 reverse 시 [::-1]의 사용은 지양하자
'''
def solution(n, t, m, p):
    answer = ''
    totalNumber = []

    # 1000 * 100
    for eachNumber in range(t * m):
        temp = []
        if eachNumber == 0:
            totalNumber.append("0")
            continue

        # 1000 * 100
        while eachNumber != 0:
            leaveValue = eachNumber % n
            if leaveValue == 10:
                temp.append('A')
            elif leaveValue == 11:
                temp.append('B')
            elif leaveValue == 12:
                temp.append('C')
            elif leaveValue == 13:
                temp.append('D')
            elif leaveValue == 14:
                temp.append('E')
            elif leaveValue == 15:
                temp.append('F')
            else:
                temp.append(leaveValue)
            eachNumber //= n

        temp = list(map(str, temp))
        temp.reverse()
        totalNumber.append("".join(temp))
    print("totalNumber = ", totalNumber)
    totalNumber = "".join(totalNumber)
    print("totalNumber = ", totalNumber)


    for i in range(len(totalNumber)):
        if len(answer) != t:
            # 자른 것에 몇번째를 표현
            if len(totalNumber[:i]) % m == (p - 1):
                answer += totalNumber[i]
        if len(answer) == t:
            break

    return answer


# 진법, 미리구할숫자, 참가인원, 참가인원, 순서
print(solution(2, 4, 2, 1)) # "0111"
print(solution(16, 16, 2, 1)) # "02468ACE11111111"
print(solution(16, 16, 2, 2))  # "13579BDF01234567"
