'''
문제 : 롤케이크 자르기
'''
from collections import Counter
def solution(topping):
    answer = 0
    setTopping = set(topping)

    for i in range(len(topping) - 1):
        old = set(topping[:i+1])
        young = set(topping[i+1:])
        if len(old) == len(young):
            answer += 1
    return answer

def solutionCounter(topping):
    old = Counter(topping)
    young = set()
    answer = 0

    for i in topping:
        old[i] -= 1
        young.add(i)
        if old[i] == 0:
            old.pop(i)
        if len(old) == len(young):
            answer += 1
    return answer

if __name__ == '__main__':
    print(solutionCounter([1, 2, 1, 3, 1, 4, 1, 2]))
