'''
N^2을 logN으로 만드는 방법 : 이분탐색
N^2을 N으로 만드는 방법 : Two Pointer
'''
from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)  # 초기 들어오는 queue1, queue2의 길이는 같습니다.
    queue2 = deque(queue2)
    queue1Sum = sum(queue1)
    queue2Sum = sum(queue2)

    print(type(sum(queue1)))
    result = 0

    for i in range(len(queue1) * 3):
        if queue1Sum > queue2Sum:
            temp = queue1.popleft()
            queue1Sum -= temp
            queue2Sum += temp
            queue2.append(temp)
        elif queue1Sum < queue2Sum:
            temp = queue2.popleft()
            queue1Sum += temp
            queue2Sum -= temp
            queue1.append(temp)
        else:
            return answer
        answer += 1
    else:
        return -1
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
