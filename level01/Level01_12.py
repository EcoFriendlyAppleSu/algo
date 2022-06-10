# 실패율

def solution(N, stages):
    answer = []
    tempAry = [0] * (N + 2)
    length = len(stages)

    for i in stages: # 1 ~ 6
        tempAry[i] += 1

    for i in range(1, len(tempAry)):
        temp = length
        temp = length - tempAry[i]
        tempAry[i] = tempAry[i] / length
        length = temp

    tempAry = tempAry[1:len(tempAry)-1]
    print(tempAry)

    answer = list(enumerate(tempAry, start=1))
    answer = sorted(answer, key= lambda x:-x[1])
    answer = dict(answer)
    answer = list(answer.keys())
    return answer

def solution2(n, stages):
    answer = []
    value = len(stages)
    temp_dict = {}

    for x in range(1, n+1):
        count = 0

        for y in stages:
            if x == y:
                count += 1
        if count != 0:
            temp_dict[x] = count / value
            value = value - count
        else:
            temp_dict[x] = 0

    result = dict(sorted(temp_dict.items(), reverse=True, key= lambda x:x[1]))
    answer = list(result.keys())

    return answer

if __name__ == '__main__':
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))
