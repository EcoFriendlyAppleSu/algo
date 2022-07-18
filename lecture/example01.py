def solution(mylist):
    answer = []
    temp = 0
    for i in mylist:
        for j in i:
            temp += 1
        answer.append(temp)
        temp = 0

    return answer

def solutionMorePythonable(mylist):
    return list(map(len, mylist)) # map 요소 하나하나에 접근할거란 의미

# iterable : 자신의 맴버를 한 번에 하나씩 리턴할 수 있는 객체. list, str, tuple, dict 등이 속함
# sequence : int type index를 통해 원소에 접근할 수 있는 iteralbe
if __name__ == '__main__':
    input = [[1, 2], [3, 4], [5]]
    print(*input)
    print(solution(input))
    print(solutionMorePythonable(input))
