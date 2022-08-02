# 순위 검색
# 해당 문제는 더 생각이 필요하다.
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

# 시간 초과 풀이, 그치만 논리는 맞다
def solution(info, query):
    answer = []
    for q in query:
        q = q.replace("and", "")
        q = q.split()
        count = 0
        for i in info:
            i = i.split()
            flag = True
            if int(i[4]) < int(q[4]):
                flag = False
            else:
                for index in range(4):
                    if q[index] == "-":
                        continue
                    else:
                        if q[index] != i[index]:
                            flag = False
                            break
            if flag:
                count += 1
        answer.append(count)
    return answer

# binary search로 문제 해결
def solutionUsingBinary(information, queries):
    answer = []
    dic = defaultdict(list) # 기본값을 딕셔너리값의 초기값으로 지정할 수 있다.
    for info in information: # information을 하나씩 가져온다.
        info = info.split() # split 진행
        condition = info[:-1] # 마지막 값인 값을 저장
        score = int(info[-1]) # score에 str -> int 형변환, 저장
        for i in range(5): # 모든 조합을 포함한 dictionary 생성
            case = list(combinations([0,1,2,3], i)) # ?
            for c in case:
                temp = condition.copy()
                for index in c:
                    temp[index] = "-"
                key = ''.join(temp) # 모든 경우의 수에 대해서 "".join을 통해 문자열 하나로 통합
                dic[key].append(score)

    for value in dic.values(): # Value에 따라 정렬
        value.sort()

    for query in queries: # query
        query = query.replace("and ", "")
        query = query.split()
        targetKey = ''.join(query[:-1])
        targetScore = int(query[-1])
        count = 0

        if targetKey in dic:
            targetList = dic[targetKey]
            index = bisect_left(targetList, targetScore)
            count = len(targetList) - index
        answer.append(count)
    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))
    print(solutionUsingBinary(info, query))