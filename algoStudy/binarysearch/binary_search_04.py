'''
프로그래머스 문제 : 징검다리 건너기
'''

def solution(stones, k):
    left = 1
    right = 200000000 # 디딜 수 있는 횟수

    while left <= right:
        mid = (left + right) // 2 # 건널 수 있는 횟수인 mid
        count = 0
        for stone in stones: # 디딤돌을 순회하면서
            if stone - mid <= 0: # 건널 수 있는 지 판단하고
                count += 1 # 건널 수 없다면 count += 1
            else: # 건널 수 있다면
                count = 0 # 0으로 초기화
            if count >= k: # 만약 k 이상 디딤돌이 거리가 있다면
                break # loop 탈출
        if count >= k: # 만약 k 이상 디딤돌이 거리가 있다면
            right = mid - 1 # 디딤 횟수를 줄입니다.
        elif count < k: # k 보다 작다면
            left = mid + 1 # 디딤 횟수를 늘립니다.
    return left # 디딤 횟수를 최대한 늘렸을 때 값이 최대값입니다.

if __name__ == '__main__':
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))