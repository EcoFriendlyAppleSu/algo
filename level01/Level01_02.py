# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    hit = 0
    hasZero = 0
    rank = 7
    answer = []
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)

    for i in lottos:
        if i in win_nums:
            hit += 1
        elif i == 0:
            hasZero += 1

    if hit > 0 or hasZero > 0:
        answer.append(rank - hit - hasZero)
    else:
        answer.append(6)

    if hit == 0:
        answer.append(6)
    else:
        answer.append(rank - hit)

    return sorted(answer)

if __name__ == '__main__':
    lottos = [45, 4, 35, 20, 3, 9]
    win_nums = [45, 4, 35, 20, 3, 9]
    print(solution(lottos, win_nums))
