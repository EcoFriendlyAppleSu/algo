# 시계에 3이 얼마나 들어있나요?
# 이 문제는 완전 탐색에 적합한 문제입니다. 반복하는 횟수의 양이 100,000 아래라 완전 탐색으로 해결할 수 있다.
# 시간 복잡도를 생각해 보자

hour = int(input())

count = 0

for i in range(hour):
    for j in range(24):
        for k in range(60):
            for r in range(60):
                if '3' in str(j) + str(k) + str(r):
                    count += 1
print(count)