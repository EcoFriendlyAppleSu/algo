# 무지의 먹방 라이브
import heapq


def solution(foodTime, k):
    answer = -1
    if sum(foodTime) <= k:
        return answer
    queue = []
    for i in range(len(foodTime)):
        # queue에 (음식 총 시간, 음식 순서)를 입력해 음식 총시간에대한 오름차순으로 정렬
        heapq.heappush(queue, (foodTime[i], i + 1))

    foodNumber = len(foodTime)
    previous = 0

    while queue:
        # 걸리는 시간 * 남은 음식의 수
        time = (queue[0][0] - previous) * foodNumber
        if k >= time:
            k -= time
            previous, _ = heapq.heappop(queue)
            foodNumber -= 1
        else:
            # noise 시간 K와 남은 음식의 수를 알면 몇 번째 음식이 다음에 먹을 음식인지 알 수 있습니다.
            index = k % foodNumber
            # 음식의 가중치대로 queue를 정렬 (음식 시간, 음식 순서)는 바뀌지 않고 정렬만 음식 순서 기준으로 바뀝니다.
            queue.sort(key=lambda x: x[1])
            answer = queue[index][1]
            break
    return answer


if __name__ == '__main__':
    foodtime = [3, 1, 2]
    k = 5
    print(solution(foodtime, k))
