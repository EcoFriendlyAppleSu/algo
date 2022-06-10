# 약수의 개수와 덧셈

def judgeNumberEvenOrOdd(number):
    ary = []

    for i in range(1, (number //2) + 1):
        if (number % i) == 0:
            ary.append(i)

    ary.append(number)
    print(ary)

    if len(ary) % 2 == 0:
        return True
    else:
        return (-1)

    return None
def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        answer += ( i * judgeNumberEvenOrOdd(i))

    return answer

if __name__ == '__main__':
    left = 13
    right = 17
    print(solution(left,right))
