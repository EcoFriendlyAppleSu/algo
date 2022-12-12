def solution(cards):
    answer = 1
    tempList = []
    result = []
    visited = [False] * len(cards)
    for i in range(len(cards)):
        cards[i] -= 1

    for i in range(len(cards)):
        index = i
        temp = []
        while visited[index] == False:
            visited[index] = True
            temp.append(index)
            index = cards[index]
        if len(temp) == 0:
            continue
        tempList.append(temp)
    print(tempList)

    for i in tempList:
        result.append(len(i))

    result.sort()
    print(result)
    if len(result) == 1:
        answer = 0
    else:
        answer = result[-1] * result[-2]

    return answer


solution([8,6,3,7,2,5,1,4])