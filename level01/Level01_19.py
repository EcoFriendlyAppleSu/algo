# 연속된 두 수의 합
def solution(num, total):
    answer = []

    temp = 0
    count = 0
    for i in range(num):
        temp += i
        count += 1
    total -= temp
    startValue = total // count
    print(startValue)

    for i in range(count):
        answer.append(startValue + i)

    return answer

if __name__ == '__main__':
    print(solution(3, 12))