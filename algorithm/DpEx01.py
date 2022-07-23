# 계단 오르기 최소 비용

def solution(givenCosts):
    case1 = 0
    case2 = 0
    current = 0

    for i in range(len(givenCosts)-1, -1, -1):
        current = givenCosts[i] + min(case1, case2)
        case2 = case1
        case1 = current

    return min(case1, case2)


if __name__ == '__main__':
    givenCosts = [1,100,1,1,1,100,1,100,1]
    print(solution(givenCosts))