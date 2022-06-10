# 숫자 문자열과 영단어

def solution(s):
    answer = 0
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for number in range(len(numbers)):
        if numbers[number] in s:
            s = s.replace(numbers[number], str(number))

    answer = int(s)
    return answer

if __name__ == '__main__':
    s = "2three45sixseven"
    print(solution(s))