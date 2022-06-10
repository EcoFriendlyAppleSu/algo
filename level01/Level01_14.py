# 3진법 뒤집기


def solution(number):
    answer = 0
    tempList = []
    while True:
        temp = number % 3 # 3 나눈 나머지
        number = number // 3 # 3 으로 나눈 값
        tempList.append(temp)
        if number == 0:
            break
    tempList = list(reversed(tempList))
    print(tempList)

    for i in range(len(tempList)):
        answer += (tempList[i] * (3**i))

    return answer


if __name__ == '__main__':
    n = 125
    print(solution(n))

# 45 // 3 => 15
# 15 // 3 => 5
# 5 // 3 => 1
# 1 // 3 => 0