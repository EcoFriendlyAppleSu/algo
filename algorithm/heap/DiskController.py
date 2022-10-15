# 프로그래머스 Disk Controller
import heapq

def solution(jobs):
    answer = 0
    end, i = 0,0
    start = -1
    queue = []

    while len(jobs) > i:
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(queue, (job[1], job[0]))
        if len(queue) > 0:
            now = heapq.heappop(queue)
            start = end
            end += now[0]
            answer += (end - now[1])
            i += 1
        else:
            end += 1
    resu

if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]
    solution(jobs)