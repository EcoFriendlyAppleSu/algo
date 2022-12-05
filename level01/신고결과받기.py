from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    overK = []
    holtUser = defaultdict(list)
    reportedList = defaultdict(int)
    report = set(report)  # 중복 처리
    print("report = ", report)

    # 1000
    for id in id_list:
        reportedList[id] = 0 # report =  {'muzi frodo', 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi'}
        holtUser[id]

    # 21
    for element in report:
        reporter, reportee = element.split(" ")
        reportedList[reportee] += 1
        holtUser[reporter].append(reportee)
    reportedList = list(reportedList.items()) # reportedList items =  [('muzi', 1), ('frodo', 2), ('apeach', 0), ('neo', 2)]
    print("reportedList items = ", reportedList)

    # 1000
    for element in reportedList:
        if element[1] >= k:
            overK.append(element[0]) # overK =  ['frodo', 'neo']
    print("overK = ", overK)

    print("holtUser = ", holtUser)
    holtUser = list(holtUser.items())

    # 1000
    for i in range(len(holtUser)):
        reporteeList = holtUser[i][1]
        # 1000
        for j in range(len(reporteeList)):
            print(reporteeList[j])
            if reporteeList[j] in overK:
                answer[i] += 1

    return answer


if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
                   2))
