# 소수 찾기
from itertools import permutations, chain
import math

def judgePrimeNumber(number):
    flag = 0
    number = int(number)
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) +1)):
        if number % i == 0:
            flag += 1
            continue
    if flag == 0:
        return True
    else:
        return False

def solution(numbers):
    answer = 0
    permutatedNumbers = list(chain.from_iterable(permutations(numbers, r) for r in range(1, len(numbers) + 1)))

    permutatedNumbers = list(map(list, permutatedNumbers))

    for i in permutatedNumbers:
        if i[0] == '0':
            i.pop(0)

    # set을 구하는 방식
    setedNumbers = set(map("".join, permutatedNumbers))
    print(setedNumbers)
    setedNumbers = list(map(int, setedNumbers))

    # Define Prime number
    for i in setedNumbers:
        if judgePrimeNumber(i):
            answer += 1
    return answer


def checkPrime(number):
    if number <2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solutionOther(numbers):
    answer = []
    numbers = list(numbers)
    print(numbers)
    temp = []

    for i in range(1, len(numbers) +1): # chain ing
        temp += list(permutations(numbers, i))
    num = [int(''.join(t)) for t in temp]
    print(set(num))

    for i in num:
        if checkPrime(i):
            answer.append(i)
    return len(set(answer))
if __name__ == '__main__':
    numbers = "1111"
    print(solutionOther(numbers))
    print(solution(numbers))