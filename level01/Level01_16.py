# 나머지가 1이 되는 수

def solution(n):
    answer = 0
    temp = []
    for i in range(1, n):
        if n % i == 1:
            temp.append(i)
    answer = max(temp)
    return answer


if __name__ == '__main__':
    n = 12
    print(solution(n))
