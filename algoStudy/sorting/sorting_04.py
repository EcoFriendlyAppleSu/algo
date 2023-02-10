'''
프로그래머스 문제 : 기지국 설치
'''

'''
N <= 200,000,000
stations <= 10,000
w <= 10,000
'''
from math import ceil
def solution(n, stations, w):
    answer = 0
    positions = [0]
    stations.append(n)
    positions.extend(stations)
    dividdValue = 2*w + 1
    for i in range(len(positions) -1):
        if positions[i] == 0:
            prePosition = positions[i] + 1
        else:
            prePosition = positions[i] + w
        postPosition = positions[i+1] - w
        if prePosition > postPosition:
            break
        temp = postPosition - prePosition + 1
        value = ceil(temp / dividdValue)
        if value == 0:
            answer += 1
        else:
            answer += value
    return answer

def solution2(n, stations, w):
    answer = 0
    W = 2 * w + 1

    start = 1
    # 10,000
    for s in stations:
        answer += max(ceil((s - w - start) / W), 0)
        start = s + w + 1

    if n >= start:
        answer += ceil((n - start + 1) / W)

    return answer
if __name__ == '__main__':
    print(solution2(11, [4,11], 1))
    print(solution2(16, [9], 2))
