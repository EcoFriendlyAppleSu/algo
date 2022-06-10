# 부족한 금액 계산

def solution(price, money, count):
    temp = 0
    for i in range(1, count+1):
        temp += price * i

    if (temp - money) > 0:
        return temp - money
    else:
        return 0


if __name__ == '__main__':
    price = 3
    money = 20
    count = 4
    print(solution(price, money, count))