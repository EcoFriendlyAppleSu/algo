'''
다리를 지나는 트럭
'''
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)  # [7,4,5,6]
    compareBridge = [0] * bridge_length  # [0,0,0,0]
    bridge_length = deque([0] * bridge_length)  # [0,0,0,0]
    zeroValue = 0

    while sum(queue) != 0:
        currentTruck = queue[0]
        if sum(bridge_length) + currentTruck <= weight:
            currentTruck = queue.popleft()
            queue.append(zeroValue)
            bridge_length.popleft()
            bridge_length.append(currentTruck)
            answer += 1
        else:
            bridge_length.popleft()
            bridge_length.append(zeroValue)
            answer += 1

        if sum(bridge_length) == 0:
            answer -= 1
        print("bridge_length = ", bridge_length)

    while sum(bridge_length) != 0:
        bridge_length.popleft()
        bridge_length.append(zeroValue)
        answer += 1
    print("bridge_length = ", bridge_length)
    print(answer)
    return answer

def solution2(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    time = 0
    index = 0
    sum = 0

    while True:
        time += 1
        sum -= queue.pop(0)
        if index < len(truck_weights):
            if truck_weights[index] + sum <= weight:
                sum += truck_weights[index]
                queue.append(truck_weights[index])
                index+=1
            else:
                queue.append(0)
        else:
            time += bridge_length -1
            break
    return time

# solution(2, 10, [7, 4, 5, 6])
solution2(5, 5, [2,2,2,2,1,1,1,1,1])
# solution(10000, 10000, [1,1,1,1,1,1,1,10000,9999,9998,1])

# solution(100, 100, [10])
# solution(100, 100, [10,10,10,10,10,10,10,10,10,10])


'''
    while queue != compareBridge: # 브릿지와 큐의 값이 다를 때
        currentTruck = queue[0]
        if sum(bridgeQueue) + currentTruck <= weight:
            currentTruck = queue.popleft()
            queue.append(zeroValue)
            bridgeQueue.append(currentTruck)
            bridgeQueue.popleft()
            answer += 1
        else:
            bridgeQueue.append(zeroValue)
            bridgeQueue.popleft()
            answer += 1

        if sum(queue) == 0:
            break
    print("bridgequeue = ", bridgeQueue)
    while sum(bridgeQueue) != 0:
        bridgeQueue.append(zeroValue)
        bridgeQueue.popleft()
        answer += 1

    print("answer = ", answer)'''
