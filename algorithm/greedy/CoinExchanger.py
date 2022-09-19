# 당장 좋은 것만 선택하는 그리디

def solution():
    money = int(input("10의 배수로 숫자를 입력해 주세요 :"))
    count = 0
    while money > 0:
        if (money // 500) > 0:
            count += (money // 500)
            money = (money % 500)
            continue
        elif (money // 100) > 0:
            count += (money // 100)
            money = (money % 100)
            continue
        elif (money // 50) > 0:
            count += (money // 100)
            money = (money % 100)
            continue
        else:
            count += (money // 10)
            break
    return count

def pythonableSolution():
    money = 1460
    count = 0
    coin_type = [500,100,50,10]

    for coin in coin_type:
        count += money // coin
        money %= coin
    return count



if __name__ == '__main__':
    print(pythonableSolution())
    # print(solution())