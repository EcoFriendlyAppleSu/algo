# 신고 결과 받기
from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    reportedList = defaultdict(set)
    reporterList = defaultdict(set)

    for index in report:
        reporter, reported = index.split(" ")
        reportedList[reporter].add(reported)
        reporterList[reported].add(reporter)

    print(reportedList)
    print(reporterList)

    for id in id_list:
        count = 0
        for index in reportedList[id]:
            if len(reporterList[index]) >= k:
                count += 1
        answer.append(count)



    return answer


if __name__ == '__main__':
    idList = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    sueTime = 2
    print(solution(idList, report, sueTime))


# dictionary init
# idList = ["muzi", "frodo", "apeach", "neo"]
# idDict = {}
# for i in idList:
#     idDict[i] = ""
# dictionary key, value 일대일 대응
# 꺼내서 사용하려면 중간에 tempSet을 두고 사용해야한다.
# set은 add를 사용한다.
# defaultdictionary에 대해 잘 알아두자
