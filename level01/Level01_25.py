'''
문제 : 숫자 짝꿍
'''

from itertools import permutations


def solution(X, Y):
    answer = []
    for i in (set(X) & set(Y)):
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)
    answer.sort(reverse=True)
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    answer = "".join(answer)
    return answer

if __name__ == '__main__':
    print(solution("5525", "1255"))