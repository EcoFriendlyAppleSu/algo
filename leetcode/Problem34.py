# Find First and Last Position of Element in Sorted Array

def solution(nums, target):
    indexAry = []
    answer = []
    for i in range(len(nums)):
        if nums[i] == target:
            indexAry.append(i)
    print(indexAry)

    if len(indexAry) == 0:
        indexAry.extend([-1])

    answer.extend([indexAry[0], indexAry[-1]])

    print(answer)

def solutionUsingBinarySearch(nums, target):
    pass

if __name__ == '__main__':
    nums = [1]
    target = 1
    solution(nums, target)
