'''
문제 : 비밀지도
풀이 정리. 답은 이진 계산에 있어
'''

def numberToBinary(number, n):
    binary = []
    while number > 0:
        binary.append(number % 2)
        number //= 2
    while len(binary) < n:
        binary.append(0)
        if len(binary) == n:
            break
    return list(reversed(binary))

def solution(n, arr1, arr2):
    answer = []
    array1 = []
    array2 = []
    result = []

    for i in range(n):
        array1.append(numberToBinary(arr1[i], n))
        array2.append(numberToBinary(arr2[i], n))

    print(array1)
    print("-----")
    print(array2)

    for i in range(n):
        temp = []
        for j in range(n):
            if (array1[i][j] | array2[i][j]) == True:
                temp.append("#")
            else:
                temp.append(" ")
        answer.append(temp)

    for i in range(n):
        result.append("".join(answer[i]))

    return result

if __name__ == '__main__':
    # print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))


'''
import copy

def solution(n, arr1, arr2):
    ary1_binary = []
    ary2_binary = []
    temp = []
    result = []

    for x in arr1:
        while x > 0:
            temp.append(x%2)
            x = x // 2
        temp = list(reversed(temp))
        if len(temp) != n:
            for x in range(n-len(temp)):
                temp = [0] + temp
        ary1_binary.append(copy.deepcopy(temp))
        temp.clear()

    for x in arr2:
        while x > 0:
            temp.append(x%2)
            x = x // 2
        temp = list(reversed(temp))
        if len(temp) != n:
            for x in range(n-len(temp)):
                temp = [0] + temp
        ary2_binary.append(copy.deepcopy(temp))
        temp.clear()

    for x in range(len(ary1_binary)):
        result.append(list(map(lambda x,y:x|y, ary1_binary[x],ary2_binary[x])))

    for x in range(len(result)):
        for y in range(n):
            if result[x][y] == 1:
                result[x][y] = '#'
            else:
                result[x][y] = ' '

    for x in range(len(result)):
        result[x] = "".join(result[x])

    return result
'''