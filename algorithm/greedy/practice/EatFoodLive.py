# 무지의 먹방 라이브
def solution(foodTimes, k):
    result  = 0
    index = 0
    while k >= 0:
        foodTimes[index] -= 1
        k -= 1
        index += 1
        if index == len(foodTimes):
            index = 0
    print(index + 1)
    return None

if __name__ == '__main__':
    foodTimes = [3,1,2]
    k = 5
    solution(foodTimes, k)