'''
튜플 문제입니다.
'''
def solution(s):
    answer = []
    s = s[2:-2]
    temp = []
    s = list(s.split("},{"))

    for index in s:
        index = list((index.split(",")))
        temp.append(index)

    temp.sort(key=len)

    print("temp = ", temp)

    # 100,000
    for i in temp:
        # 100,000
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
    return answer


if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    # print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
