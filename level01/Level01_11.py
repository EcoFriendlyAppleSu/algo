# 모의고사

# enumerate ?
def solution(answers):
    answer = []
    count = [0,0,0]
    fstStudent = [1, 2, 3, 4, 5]
    sndStudent = [2,1,2,3,2,4,2,5]
    trdStudent = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        print(i)
        if fstStudent[i%len(fstStudent)] == answers[i]:
            count[0] += 1
        if sndStudent[i%len(sndStudent)] == answers[i]:
            count[1] += 1
        if trdStudent[i%len(trdStudent)] == answers[i]:
            count[2] += 1

    for index, cnt in enumerate(count):
        if cnt == max(count):
            answer.append(index +1)

    return answer
if __name__ == '__main__':
    answer = [1,2,3,4,5]
    print(solution(answer))
