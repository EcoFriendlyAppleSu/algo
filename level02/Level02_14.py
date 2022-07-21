# 가장 큰 수
from itertools import permutations

# 기존 풀이 -> 경우의 수가 많아져 시간 초과가 발생한다.
def solution(numbers):
    answer = ''
    stringNumbers = list(map(str, numbers))

    permutatedNumbers = list(permutations(stringNumbers, len(stringNumbers)))

    resultNumbers = []

    for i in permutatedNumbers:
        resultNumbers.append(int("".join(i)))

    print(resultNumbers)
    answer = str(max(resultNumbers))
    return answer

# 경우의 수를 줄인 파이썬스러운 코드
# 숫자 문자열을 sorting할 땐 앞의 숫자를 기준으로 비교해서 정렬해준다.
def solutionWithoutPermutation(numbers):
    strNumbers = list(map(str, numbers))
    strNumbers.sort(key=lambda x: x*3, reverse=True) # sorted와는 다르게 기존 문자열에 영향을 끼친다.
    return str(int("".join(strNumbers)))

if __name__ == '__main__':
    numbers = [0,0,0,0]
    print(solutionWithoutPermutation(numbers))


