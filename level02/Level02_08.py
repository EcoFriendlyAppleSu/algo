# 괄호 변환

# 문자열을 u, v로 분리하는 메소드
def divide(strings):
    openBracket = 0
    closeBracket = 0

    for i in range(len(strings)):
        if strings[i] == '(':
            openBracket += 1
        else:
            closeBracket += 1
        if openBracket == closeBracket:
            return strings[:i + 1], strings[i+1:]

# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def check(strings):
    stack = []

    for i in strings:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack: # if stack is False
                return False
            stack.pop()
    return True

def solution(strings):
    # process 1
    if not strings: # if not의 질의가 False일 때, 진행된다.
        return ""
    # process 2
    u, v = divide(strings)

    # process 3
    if check(u) is True: # stack을 돌렸을 때 값이 True 면
        return u + solution(v) # u가 True일 때, v를 solution에 v를 넣어 재귀 처리
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for index in u[1:len(u) -1]:
            if index == '(':
                answer += ')'
            else:
                answer += '('
        return answer

if __name__ == '__main__':
    # strings = ")("
    strings = "(()())()"
    print(solution(strings))
