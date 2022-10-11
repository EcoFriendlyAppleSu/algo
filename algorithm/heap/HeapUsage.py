# 기본적인 힙 사용법
import heapq

# heap binary tree 생성 후 왼쪽 위부터 채워나감 자동적으로 heapify가 된다
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 0)
print(heap)

# heap 원소 삭제, 얻기
print(heapq.heappop(heap))
print(heap) # return 0

print(heapq.heappop(heap))
print(heap) # return 1

# heap peek
print(heap[0]) # return 4

# heapq는 기본적으로 오름차순으로 진행된다. 즉, 최소힙으로 tree가 만들어진다.
nums = [4, 1, 7, 3, 8, 5]
maxHeap = []
# sort method의 reversed 처럼 트릭을 넣어 최대힙으로 만들 수 있다.
for num in nums:
    # (우선순위, 값), 즉 음수를 취하게되어 값이 큰 만큼 최소값이 되어 상단에 올라간다.
    # 첫 번째 인자값으로 heap을 정리
    heapq.heappush(maxHeap, (-num, num))

# 최대힙을 구하는 방법. !주의해야할 점 = index에 접근할 때 heap에서 tuple을 꺼내고 index를 찾아야한다.
print(maxHeap)
while maxHeap:
    print(heapq.heappop(maxHeap)[1], end=' ')
