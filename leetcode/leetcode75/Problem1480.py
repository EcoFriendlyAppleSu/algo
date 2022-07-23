from itertools import accumulate

def solution(nums):
    answer = []
    temp = 0
    for i in nums:
        temp += i
        answer.append(temp)
    return answer

def solutionUsingAccumulate(nums):
    return list(accumulate(nums))

def solutionUsingArySlice(nums):
    return [sum(nums[:i]) for i in nums]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(solution(nums))
    print(solutionUsingAccumulate(nums))
    print(solutionUsingArySlice(nums))
