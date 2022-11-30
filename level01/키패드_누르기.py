def solution(numbers, hand):
    currentLeft = 10
    currentRight = 12
    phone = [[1,2,3], [4,5,6], [7,8,9], [10, 0, 12]]
    leftAry = [1,4,7]
    rightAry = [3,6,9]
    middleAry = [2,5,8,0]
    answer = ''
    for element in numbers:
        # 1,4,7일 경우 "L" append
        if element in leftAry:
            answer += "L"
            currentLeft = element
            continue
        # 3,6,9일 경우 "L" append
        if element in rightAry:
            answer += "R"
            currentRight = element
            continue

        # 2,5,8,0일 경우
        if element in middleAry:
            middleColumn, middleRow = 1, 0
            leftColumn, leftRow = 0,0
            rightColmn, rightRow = 0,0

            for i in range(len(phone)):
                if element in phone[i]:
                    middleRow = i
                    break

            for i in range(len(phone)):
                if currentLeft in phone[i]:
                    leftRow = i
                    for j in range(len(phone[i])):
                        if currentLeft == phone[i][j]:
                            leftColumn = j
                            break
                    break

            for i in range(len(phone)):
                if currentRight in phone[i]:
                    rightRow = i
                    for j in range(len(phone[i])):
                        if currentRight == phone[i][j]:
                            rightColmn = j
                            break
                    break
            leftValue = abs(leftRow - middleRow) + abs(leftColumn - middleColumn)
            rightValue = abs(rightRow - middleRow) + abs(rightColmn - middleColumn)

            if leftValue < rightValue:
                answer += "L"
                currentLeft = element
                continue
            elif leftValue > rightValue:
                answer += "R"
                currentRight = element
                continue
            elif leftValue == rightValue:
                if hand == "right":
                    answer += "R"
                    currentRight = element
                    continue
                else:
                    answer += "L"
                    currentLeft = element
                    continue

    return answer
# 시간 복잡도 O(n + 4*4*3*2)
# worst case -> n : 1000, 시간 복잡도 : 1096

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))
