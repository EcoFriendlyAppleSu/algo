# 최소 직사각형

def solution(size):
    answer = 0
    for index in size:
        if index[0] >= index[1]:
            temp = index[0]
            index[0] = index[1]
            index[1] = temp
    print(size)
    width =  max(size, key=lambda x:x[0])
    height = max(size, key=lambda x:x[1])
    print(width, height)
    answer = width[0] * height[1]
    return answer


if __name__ == '__main__':
    size = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(size))
