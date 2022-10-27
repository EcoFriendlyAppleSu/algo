'''
문제 : 괄호 변환
'''
from collections import deque


def balancedIndex(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def judgeRightString(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(string):
    answer = ''
    if string == '':
        return answer
    index = balancedIndex(string)
    u = string[:index + 1]
    v = string[index + 1:]

    if judgeRightString(string):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer


if __name__ == '__main__':
    string = "()))((()"
    print(solution(string))
