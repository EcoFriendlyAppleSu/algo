def divide(string):
    left = 0
    right = 0

    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return string[: i + 1], string[i+1:]

def check(string):
    stack = []

    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) <= 0:
                return False
            stack.pop()
    return True

def solution(string):

    if string == "":
        return ""
    u, v = divide(string)

    if check(u) is True:
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for string in u[1:len(u) -1]:
            if string == '(':
                answer += ')'
            else:
                answer += '('
        return answer


print(solution(""))
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))