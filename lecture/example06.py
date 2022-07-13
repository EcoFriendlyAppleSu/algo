# 원본을 유지한 정렬된 리스트 구하기

# list1 = [3,2,5,1]
# list2 = sorted(list1)
# print(list1)
# print(list2)

# zip은 각 iterables의 요소들을 모으는 이터레이터를 만듭니다.
# Asterisk는 unpacking의 역할을 수행합니다.
def solution(mylist):
    answer = list(map(list, zip(*mylist))) # unpacking
    print(answer)

def solutionStandardLanguage(mylist):
    answer = [[],[],[]]

    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            answer[i].append(mylist[j][i])
    print(*answer)

if __name__ == '__main__':
    mylist =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # solution(mylist)
    solutionStandardLanguage(mylist)
