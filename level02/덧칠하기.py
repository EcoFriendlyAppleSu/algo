'''
프로그래머스 문제 덧칠하기
'''
from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section)
    while section:
        startPosition = section.popleft()

        while section and startPosition + m > section[0]:
            section.popleft()
        answer += 1
    return answer

if __name__ == '__main__':
    n = 8
    m = 4
    section = [2, 3, 6]

    solution(n,m,section)

'''
8	4	[2, 3, 6] 2
5	4	[1, 3] 1
4	1	[1, 2, 3, 4] 4
'''