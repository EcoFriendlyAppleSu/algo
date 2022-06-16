# # 오픈 채팅방
#
# def solution(record):
#     answer = []
#     dic = {} # dictionary는 가장 최근의 값을 저장한다.
#     enterString = "님이 들어왔습니다."
#     leaveString = "님이 나갔습니다."
#
#     for index in record:
#         eachIndex = index.split()
#         if len(eachIndex) == 3:
#             dic[eachIndex[1]] = eachIndex[2]
#
#     print(dic)
#
#     for sentence in record:
#         sentenceSplit = sentence.split()
#         if sentenceSplit[0] == "Enter":
#             answer.append("{}님이 들어왔습니다.".format(dic[sentenceSplit[1]]))
#         elif sentenceSplit[0] == "Leave":
#             answer.append("{}님이 나갔습니다.".format(dic[sentenceSplit[1]]))
#
#     return answer

def solution(record):
    answer = []
    dic = {}
    for i in record:
        eachIndex = i.split()
        if len(eachIndex) == 3:
            dic[eachIndex[1]] = eachIndex[2]

    for i in record:
        eachIndex = i.split()
        if eachIndex[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(dic[eachIndex[1]]))
        elif eachIndex[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(dic[eachIndex[1]]))

    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
              "Leave uid1234","Enter uid1234 Prodo",
              "Change uid4567 Ryan"]
    print(solution(record))

