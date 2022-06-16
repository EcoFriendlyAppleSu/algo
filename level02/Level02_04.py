# # 더 맵게
#
# def solution(scoville, K):
#     answer = 0
#     scoville = sorted(scoville)
#     time = len(scoville) -1
#
#     while time > 0:
#         if scoville[0] > K:
#             break
#         mixedScoville = scoville[0] + (scoville[1] * 2)
#         answer += 1
#         scoville = scoville[2:]
#         scoville.append(mixedScoville)
#         scoville = sorted(scoville)
#         time -= 1
#     if scoville[0] < K:
#         return -1
#
#     return answer

# using heapq
import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)

    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        fstIndex = heapq.heappop(scoville)
        sndIndex = heapq.heappop(scoville)
        heapq.heappush(scoville, fstIndex + (sndIndex * 2))

        answer += 1
    return answer


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))


