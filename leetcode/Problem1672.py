def solution(accounts):
    answer = []

    for i in accounts:
        answer.append(sum(i))
    print(max(answer))

if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    solution(accounts)