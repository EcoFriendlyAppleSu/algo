import math
def solution(k, d):
    answer = 0
    positions = []

    for i in range(d+1):
        for j in range(d+1):
            positions.append((i,j))
    for position in positions:
        x,y = position
        if math.sqrt(math.pow(x,2) + math.pow(y,2)) <= d:
            if (x % k == 0) and (y % k == 0):
                answer += 1

    return answer


print(solution(2, 4))
print(solution(1, 5))
