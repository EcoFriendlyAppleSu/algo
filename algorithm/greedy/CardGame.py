# 숫자 카드 게임

def solution():
    N, M = map(int, input().split())
    # Card Deck Init
    cardSet = [list(map(int, input().split())) for _ in range(N)]
    currentMinValue = min(cardSet[0])
    for time in range(1,N):
        if currentMinValue >= min(cardSet[time]):
            continue
        else:
            temp = min(cardSet[time])
            currentMinValue, temp = temp, currentMinValue
    return currentMinValue

if __name__ == '__main__':
    print(solution())