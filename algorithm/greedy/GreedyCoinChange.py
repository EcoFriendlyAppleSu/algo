# Coin Change
# greedy algorithm은 sort가 항상 필요한거같아

def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort() # sort itself
    answer = [] # output result
    index = len(coins) -1

    while True:
        currentMoney = coins[index]
        if N >= currentMoney:
            answer.append(currentMoney)
            N -= currentMoney
        if N < currentMoney:
            index -= 1
            currentMoney = coins[index]
        if N == 0:
            break

    print(answer)

if __name__ == '__main__':
    coins = [10, 50, 3, 4, 100, 7, 18]

    coinChange(140, coins)