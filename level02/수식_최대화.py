'''
리스트엔 find 함수가 존재하지 않습니다. find 함수를 사용하고 싶다면 string type에서 사용해야합니다.
'''

from itertools import permutations

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def calculate(expression, operator):
    array = []
    temp = ""

    for i in expression:
        if i.isdigit() == True: # 문자가 숫자인지 아닌지 판단
            temp += i
        else: # 문자가 숫자가 아니라면
            array.append(temp) # 기존에 buffer(temp)에 담긴 것들을 array에 append
            array.append(i) # operator append
            temp = "" # buffer 초기화
    array.append(temp) # 마지막 버퍼에 담긴 값들을 array에 append

    for o in operator:
        stack = []
        while (len(array) != 0):
            temp = array.pop(0)
            if temp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(temp)
        array = stack
    return abs(int(array[0]))


def solution(expression):
    answer = []
    op = ['+', '-', '*']
    op = list(permutations(op, 3)) # 우선순위를 따지기 위해 모든 연산자 순위를 permutations로 생성한다.

    for i in op:
        answer.append(calculate(expression, i))

    return max(answer)

print(solution("100-200*300-500+20"))