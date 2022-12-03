def solution(survey, choices):
    score = [3, 2, 1, 0, 1, 2, 3]
    personality = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0,
                   "N": 0}
    answer = ""

    # 1000
    for index in range(len(survey)):
        left, right = survey[index][0], survey[index][1]
        choice = choices[index]-1 # 가져올 값의 위치를 얻습니다.
        choiceScore = score[choice] # 점수를 알 수 있습니다.
        if choice == 3:
            continue
        if choice < 3:
            personality[left] += choiceScore
            continue
        if choice > 3:
            personality[right] += choiceScore
            continue

    listPersonality = list(personality.items())

    # 4
    for i in range(0, len(listPersonality), 2):
        if listPersonality[i][1] >= listPersonality[i+1][1]:
            answer += listPersonality[i][0]
            continue
        answer += listPersonality[i+1][0]

    return answer


if __name__ == '__main__':
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5,3,2,7,5]))
    # print(solution(["TR", "RT", "TR"], [7, 1, 3]))
