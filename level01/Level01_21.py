'''
문제 : 성격 유형 검사
Tip : dictionary 자료 구조를 기억하고 사용하자
'''
def solution(survey, choices):
    answer = ''
    board = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i in range(len(survey)):
        left = survey[i][0]
        right = survey[i][1]
        if choices[i] - 4 > 0:
            board[right] += choices[i] - 4
        elif choices[i] - 4 < 0:
            board[left] += 4 - choices[i]

    answer += "R" if board["R"] >= board["T"] else "T"
    answer += "C" if board["C"] >= board["F"] else "F"
    answer += "J" if board["J"] >= board["M"] else "M"
    answer += "A" if board["A"] >= board["N"] else "N"
    return answer


if __name__ == '__main__':
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
