# find the pivot index

def solution(nums):
    answer = -1
    leftValue = 0
    rightValue = 0

    for i in range(len(nums)):
        leftValue = sum(nums[:i])
        rightValue = sum(nums[i+1:])
        if leftValue == rightValue:
            answer = i
    return answer

def solutionUsingenumerate(nums):
    S = sum(nums)
    leftSum = 0
    for i, x in enumerate(nums): # index, value 같이 접근하는 것
        if leftSum == (S - leftSum - x):
            return i
        leftSum += x
    return -1

if __name__ == '__main__':
    # nums = [1, 7, 3, 6, 5, 6]
    nums = [2,1,-1]
    print(solution(nums))
    print(solutionUsingenumerate(nums))
