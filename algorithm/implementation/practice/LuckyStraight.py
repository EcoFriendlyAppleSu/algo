# 럭키 스트레이트
# 문제를 잘 읽고 접근하자
# 왼쪽과 오른쪽의 덧셈만 만족하면 이라는 말이 없고 점수 N을 반으로 나누면 이라는
# 조건이 있다. 따라서 복잡하게 생각할 필요 없이 절반의 계산만 하면 된다.
number = input()
numberList = list(map(int, number))
print(numberList)
answer = ""
index = 1

while index <= len(numberList):
    preSum = 0
    postSum = 0
    for i in range(0, index):
        preSum += numberList[i]
    for i in range(index, len(numberList)):
        postSum += numberList[i]
    index += 1
    if preSum == postSum:
        answer = "LUCKY"
        break
    else:
        answer = "READY"

# 다른 답안
n = input()
length = len(n)
summary = 0

# left side number add
for i in range(length // 2):
    summary += int(n[i])

# right sit number add
for i in range(length // 2, length):
    summary -= int(n[i])

# 덧셈한 값이 0 이라면 lucky
if summary == 0:
    print("LUCKY")
else:
    print("READY")

print(answer)