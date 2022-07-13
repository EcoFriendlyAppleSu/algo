# 괄호 변환

def solution(p):
    answer = ''
    leftCursor = '('
    leftCursorCount = 0
    rightCursor = ')'
    rightCursorCount = 0

    for i in p:
        if i == leftCursor:
            leftCursorCount += 1
        else:
            rightCursorCount += 1

    if leftCursorCount == rightCursorCount:
        

if __name__ == '__main__':
    p = "(()())()"
    print(solution(p))
