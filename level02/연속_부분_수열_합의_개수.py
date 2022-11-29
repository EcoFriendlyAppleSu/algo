'''
시간 복잡도 : 1000 * 1000 + 1000 -> 1,001,000 입니다
'''

def solution(elements):
    result = []
    defaultLength = len(elements)

    for i in range(len(elements)):
        elements = elements + elements[:i]
        indexValue = i+1
        for j in range(len(elements)):
            temp = elements[j : j + indexValue]
            result.append(sum(temp))
        elements = elements[: defaultLength]
    result = set(result)

    return len(result)

print(solution([7,9,1,1,4]))
