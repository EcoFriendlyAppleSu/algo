# 기능 개발

def solution(progresses, speeds):
    answer = []

    # 만약 progresses와 speeds 길이가 같지 않다면 문제가 성립되지 않아 pass한다.
    if len(progresses) != len(speeds):
        pass

    # while 반복문을 통해 알고리즘을 진행
    while True:
        # progresses, speeds list에 접근할 index 초기화
        index = 0
        progresses = [x+y for x,y in zip(progresses, speeds)] # zip을 사용해 두 리스트를 합한 값을 progresses에 초기화

        # 만약 progresses list에 남아있는 요소가 없다면
        if len(progresses) == 0:
            break # 그대로 while 반복문 종료

        # progresses에 요소가 남아 있다면 loop 진행
        for i in progresses:
            # 만약 해당 요소가 100 이상의 값이라면
            if i >= 100:
                # index를 증가시킨다.
                index += 1
            # 100 이상의 값이 아니라면
            else:
                # 하루가 더 필요한 것으로 loop 종료
                break

        # 100 이상의 값을 가진 요소의 개수인 index를 slice에 사용해 다시 progresses에 초기화
        progresses = progresses[index:]
        # progresses 길이와 speeds의 길이는 같아야 하므로 speeds도 index를 사용해 slice
        speeds = speeds[index:]
        # 100 이상의 숫자의 개수인 index를 답인 answer list에 저장
        answer.append(index)

    # answer에 존재하는 0을 제거하는 과정
    removeSet = {0}
    answer = [i for i in answer if i not in removeSet]
    return answer

if __name__ == '__main__':
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))

