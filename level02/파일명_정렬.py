'''
sort itself
sorted needs the other var

int(stringNumber) -> 앞에 붙는 0을 제외해 나타내줍니다.
sorting lambda 의 사용

#01, result2 = list(map((lambda x: x + 2), [1, 2, 3, 4, 5]))
#02, result2 = list(filter((lambda x: x % 2 == 0), range(10)))
#03, sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))

element를 변경시킨다해서 원본 데이터가 변하는 것은 아닙니다.
'''


def solution(files):
    answer = []
    header, number, tail = '', '', ''

    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                header = file[:i]
                number = file[i:]

                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break

                answer.append([header, number, tail])
                header, number, tail = '', '', ''
                break

    answer = sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]



print(solution(["f-15"]))
print(solution(["foo010bar020.zip"]))
print(solution(
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "b-12", "F-14 Tomcat", "f-14 Tomcat"]))
