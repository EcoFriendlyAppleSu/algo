# # n진법으로 표기된 string을 10진법 숫자로 변환하기

def solution(a, b):
    output = 0
    a = list(str(a))
    for i in range(len(a)):
        output += ((int) (a[i])) * (b**(len(a)-i-1))
    return output

def solutionUsingPython(a,b):
    a = str(a) # must be string
    return type(int(a,b))


if __name__ == '__main__':
    a, b = map(int, input().strip().split(' '))
    print(solution(a,b))
    print(solutionUsingPython(a,b))




# str to each char? list
# a = 123
# a = list(str(a))
# for i in range(len(a), 0, -1): return 3 2 1
#     print(i)