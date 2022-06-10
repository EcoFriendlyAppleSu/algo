# K 번째 변수

def solution(array, commands):
    result = []
    tempAry = []
    for i, j, k in commands:
        tempAry.extend(array[i-1:j])
        tempAry.sort()
        result.append(tempAry[k-1])
        tempAry.clear()

    return result


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))
