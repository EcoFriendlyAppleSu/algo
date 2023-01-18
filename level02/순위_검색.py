'''
시간 초과 발생한 풀이
'''
def queryChange(query):
    split = list(query.split(" and "))
    temp = split[-1].split(" ")
    split = split[:3]
    split.extend(temp)
    return split # ['java', 'backend', 'junior', 'pizza', '100']


def solution(info, queries):

    answer = []
    infos = []
    for i in info:
        infos.append(i.split(" "))

    for query in queries: # ['java', 'backend', 'junior', 'pizza', '100']
        count = 0
        splitedQuery = queryChange(query)
        for info in infos: # ['java', 'backend', 'junior', 'pizza', '150']
            temp = 0
            for index in range(5):
                if splitedQuery[index] == "-": # - 일 땐, 모두 허용
                    temp += 1
                    continue
                if index == 4:
                    queryInt = int(splitedQuery[index])
                    infoInt = int(info[index])
                    if infoInt >= queryInt:
                        temp += 1
                    break
                if splitedQuery[index] == info[index]:
                    temp += 1
                else:
                    break
            if temp == 5:
                count += 1
        answer.append(count)
    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
             "- and - and - and chicken 100", "- and - and - and - 150"]
    print(solution(info, query))