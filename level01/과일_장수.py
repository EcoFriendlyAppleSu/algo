def solution(k, m, score):
    answer = 0
    amountOfBox = len(score) // m

    if len(score) < m:
        return 0

    score.sort()
    for i in range(len(score), 0, -m):
        temp = score[i - m: i]
        if len(temp) < m:
            break
        answer += min(temp) * m
    return answer


if __name__ == '__main__':
    print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
    # print(solution(4, 3, [4,1,2,2,4,4,4,4,1,2,4,2]))
