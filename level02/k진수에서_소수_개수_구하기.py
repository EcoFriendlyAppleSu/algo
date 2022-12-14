import math

def makeNumberToJinsu(n, k):
    jinsu = []
    if k == 10:
        return str(n)

    # log(1,000,000)
    while n != 0:
        jinsu.append(n%k)
        n //= k
    jinsu.reverse()
    jinsu = list(map(str, jinsu))
    return "".join(jinsu)

def isPrime(number):
    # O(1,000,000^(1/2))
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False # not prime number
    return True # prime number

def judgeNumberIsPrime(jinsu):
    result = []

    if '' in jinsu:
        return result
    jinsu = list(map(int, jinsu))
    print("prime jinsu = ", jinsu)

    # O(1) = 13
    for i in jinsu:
        if i == 1:
            continue
        if not isPrime(i):
            continue
        result.append(i)
    print("prime number list = ", result)
    return result


def judgeProblemPrimeNumber(givenNumber, primeNumbers):
    result = []
    primeNumbers = list(map(str, primeNumbers))
    print("givenNumber = ", givenNumber)
    print("primeNumbers = ", primeNumbers)

    # O(1) = 13
    for element in primeNumbers:
        if "0" + element + "0" in givenNumber:
            result.append(element)
            continue
        if element + "0" in givenNumber:
            result.append(element)
            continue
        if "0" + element in givenNumber:
            result.append(element)
            continue
        if element == givenNumber:
            result.append(element)
            continue

    return result

'''
1 ≤ n ≤ 1,000,000
3 ≤ k ≤ 10
'''
def solution(n, k):
    answer = -1

    jinsu = makeNumberToJinsu(n, k)
    print("jinsu = ", jinsu)
    compareString = jinsu

    jinsu = jinsu.split("0") # remove zero

    print("jinsu 1 = ", jinsu)

    primeNumbers = judgeNumberIsPrime(jinsu)

    result = judgeProblemPrimeNumber(compareString, primeNumbers)
    answer = len(result)
    return answer

# print(solution(143,3))
# print(solution(437674, 3))
# print(solution(110011, 10))
# print(solution(1000000, 3))
print(solution(100000000000, 10))

