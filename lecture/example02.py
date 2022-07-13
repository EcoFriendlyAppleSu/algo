def solution(n, m):
    a = str(n // m)
    b = str(n % m)
    return a + " " + b

# divmod 알아두고 map의 변환 과정을 잘 살펴보자
def solutionUsingDivmod(n,m):
    temp = list(map(str, divmod(n,m)))
    return " ".join(temp)


if __name__ == '__main__':
    n, m = map(int, input().split())
    # print(solution(n,m))
    print(solutionUsingDivmod(n,m))

