# 콜라 문제

def solution(a, b, n):
    answer = 0
    spare = 0

    while n >= a:
        answer += (n // a) * b
        spare = n % a
        n = (n // a) * b
        n += spare

    return answer

if __name__ == '__main__':
    print(solution(2,1,20))