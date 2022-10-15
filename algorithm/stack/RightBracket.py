# 옳바른 괄호

def solution(list):
    stack = []
    for i in list:
        if i == '(':
            stack.append(i)
        elif len(stack) != 0 and i == ')':
            stack.pop()
        else:
            return False
    return False if len(stack) != 0 else True

print(solution(")()("))