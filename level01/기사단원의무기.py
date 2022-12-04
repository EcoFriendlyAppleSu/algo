'''
약수 구하기 기억하자
'''
def getAttackPoint(num):
    data = set()

    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            data.add(i)
            data.add(num // i)
    return len(data)


def solution(number, limit, power):
    answer = []

    for i in range(1,number+1):
        temp = getAttackPoint(i)
        if temp > limit:
            temp = power
            answer.append(temp)
            continue

        answer.append(temp)
    print(answer)
    return sum(answer)


if __name__ == '__main__':
    print(solution(5, 3, 2))
