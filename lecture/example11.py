# 가장 많이 등장하는 알파벳 찾기
from collections import Counter

# 특정 숫자를 세야할 때 사용할 Counter library
def solution(input):
    temp = Counter(input)
    result = ''
    print(temp)

    for k, v in temp.items():
        if max(temp.values()) == v:
            result += k
    print(sorted(result)) # sorted하면 list로 나뉘어서 출력됨

def solutionWithoutPythonAPI(input):
    dict = {}
    input = list(input) # str to list

    for i in input:
        try:
            dict[i] += 1
        except KeyError:
            dict[i] = 1
    result = [ k for k, v in dict.items() if max(dict.values()) == v]
    result = sorted(result)
    return "".join(result)

if __name__ == '__main__':
    input = "bbaa"
    solution(input)
    # print(solutionWithoutPythonAPI(input))