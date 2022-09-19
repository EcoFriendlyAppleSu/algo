# 큰 수의 법칙
# 문제를 잘 읽고 풀자 : 큰 수를 고를 때 제일 큰 수를 반복학고 그 다음 수를 한 번 사용 후
# 다시 초기화되어 진행되는 것이 가장 값을 크게 가져갈 수 있는 길이다.
# 문제를 그대로 바라보고 잡음은 넣지 말아야 한다.

# 반복되는 곳을 찾아서

def mysolution():
    N = [2,4,5,4,6]
    N = sorted(N, reverse=True)
    M = 8
    K = 3
    result = 0

    first = N[0]
    second = N[1]

    while True:
        for i in range(K):
            if M == 0:
                break
            result += first
            M -= 1
        if M == 0:
            break
        result += second
        M -= 1

    return result

def pythonableSolution():
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    numbers.sort()

    firstBigData = numbers[N-1]
    secondBigData = numbers[N-2]

    # 가장 큰 수가 더해지는 횟수 계산
    # 덧셈 횟수를 반복 횟수 +1로 나눈 몫에
    count = (M // (K + 1)) * K
    count += (M % (K + 1))

    result = 0
    result += (count * firstBigData)
    result += ((M - count) * secondBigData)

    return result

if __name__ == '__main__':
    print(pythonableSolution())
    # print(mysolution())