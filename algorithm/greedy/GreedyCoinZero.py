# Coin 0

def coinChange(totalCharge, coins):
    N = totalCharge
    coins.sort()
    answer =0
    index = len(coins) -1

    while True:
        currentMoney = coins[index]
        if totalCharge >= currentMoney:
            answer += 1
            totalCharge -= currentMoney
        if totalCharge < currentMoney:
            index -= 1
            currentMoney = coins[index]
        if totalCharge == 0:
            break
    print(answer)

if __name__ == '__main__':
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    print(K)
    coinChange(K, coins)



