# tuple

# 확실하게 알아둬야 할 것은 구분자를 두 번 줘서 정렬을 할 수 있다는 것
def solution(s):
    sortedTuple = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)
    result = []
    print(sortedTuple)

    for eachTuple in sortedTuple:
        for index in eachTuple:
            if int(index) not in result:
                result.append(int(index))
                break
    return result


if __name__ == '__main__':
    givenStrings = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(givenStrings))