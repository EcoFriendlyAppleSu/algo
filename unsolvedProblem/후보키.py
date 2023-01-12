'''
풀지 못함
'''
from collections import defaultdict
from itertools import combinations
def solution(relation):
    answer = 0
    primaryList = [False] * (len(relation[0]))
    print(primaryList)


    while True:
        index = 0 # 배열 위치를 나타내는 변수
        listLength = 1
        temp = []

        for i in range(len(relation)):
            for j in range(listLength, len(relation[0]), listLength):
                temp.append(relation[i][j:j+listLength])

        setTemp = set(temp)

        if len(temp) == len(setTemp):
            answer += 1
        else:
            listLength += 1

    return answer


if __name__ == '__main__':
    print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
