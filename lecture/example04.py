# 문자열 정렬하기

def solution(strings, n):
    answer = []
    n = (int)(n) -1

    for i in range(3):  # 0 1 2
        print(("/" * (i) * (n // 2)) + strings)

# 정렬 잘 기억했다 써먹자
def solutionWithPythonMethod(strings, n):
    n = (int)(n)
    print(strings.ljust(n))
    print(strings.center(n))
    print(strings.rjust(n))


if __name__ == '__main__':
    strings, n = map(str, input().split())
    solutionWithPythonMethod(strings, n)
    # solution(strings, n)
