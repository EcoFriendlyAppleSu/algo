'''
카카오 2019 level 01
loopping을 진행할 때, 개수로 바라보는 연습을 해보자
내가 푼 문제는 시간 초과가 났다.
'''
from collections import Counter


def solution(N, stages):
    answer = []
    stageMap = dict(Counter(stages))
    clearMap = {}
    resultList = []
    resultMap = {}
    for i in range(1, N + 1):
        clearMap[i] = 0

    for i in range(1, len(clearMap)+1):
        for j in range(len(stages)):
            if i <= stages[j]:
                clearMap[i] += 1

    sortedStageMap = sorted(stageMap.items())
    sortedClearMap = sorted(clearMap.items())

    for i in range(N):
        if sortedStageMap[i][0] == sortedClearMap[i][0]:
            resultList.append(sortedStageMap[i][1] / sortedClearMap[i][1])
        else:
            resultList.append(0)
    for i in range(len(resultList)):
        resultMap[i+1] = resultList[i]
    temp = list(sorted(resultMap.items(), key= lambda x:x[1], reverse= True))

    for i in range(len(temp)):
        answer.append(temp[i][0])
    return answer

def simpleSolution(N, stages):
    result = {}
    people = len(stages)
    for stage in range(1, N + 1):
        if people != 0:
            count = stages.count(stage)
            result[stage] = count / people
            people -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x:result[x], reverse=True)


if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
