'''
문제 : 푸드 파이터 대회
'''

def solution(food):
    answer = ''
    for i in range(len(food)):
        if (food[i] // 2) <= 0:
            continue
        else:
            temp = food[i] // 2
            for j in range(temp):
                answer += str(i)
    tempResult = answer
    answer += '0'
    tempResult = list(tempResult)
    tempResult.reverse()
    answer += "".join(tempResult)
    return answer

if __name__ == '__main__':
    print(solution([1, 3, 4, 6]))