# 392 Is Subsequence
def solution(s, t):
    sDictionary = {}
    tDiscionary = {}
    for index, value in enumerate(s):
        sDictionary[value] = index
    print(sDictionary)

    for key in sDictionary.keys():
        if key in t:
            tDiscionary[key] = t.index(key)
        else:
            return False
    print(tDiscionary)

    compareDict = sorted(tDiscionary.values(), key= lambda value: value)

    if compareDict == list(tDiscionary.values()):
        return True
    else:
        return False

def solution2(s,t):
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    subsequence = 0
    # t string은 움직이지 않는 배열이야
    # 배열 s는 subsequence으로 접근할 수 있는 배열이다.
    for i in range(0, len(t)):
        if subsequence <= len(s) -1:
            print(s[subsequence])
            if s[subsequence] == t[i]:
                subsequence += 1
    return subsequence == len(s)



if __name__ == '__main__':
    s = "aaaaaa"
    t = "bbaaaa"
    print(solution2(s,t))

