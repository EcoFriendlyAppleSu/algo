def solution(new_id):
    space = " "
    idList = list(new_id)

    # 대문자 -> 소문자, 특수 문자 제거 loop
    for i in range(len(idList)):
        if str.isalpha(idList[i]) or str.isnumeric(idList[i]):
            if str.isupper(idList[i]):
                idList[i] = str.lower(idList[i])
                continue
            if str.isnumeric(idList[i]):
                continue
        else:
            if idList[i] != "-" and idList[i] != "_" and idList[i] != ".":
                idList[i] = space

    idList = "".join(idList)
    idList = idList.replace(" ", "")

    # 점 개수 관리 loop
    newList = ""
    for i in range(len(idList)):
        if len(newList) == 0:
            newList += idList[i]
            continue
        if newList[-1] == "." and idList[i] == ".":
            continue
        else:
            newList += idList[i]

    if newList[0] == ".":
        newList = newList[1:]
    if len(newList) != 0:
        if newList[-1] == ".":
            newList = newList[:len(newList)-1]
    if len(newList) == 0:
        newList += "a"

    # 16 이상이라면
    if len(newList) >= 16:
        newList = newList[:15]
        if newList[-1] == ".":
            newList = newList[:len(newList) - 1]

    while len(newList) < 3:
        newList += newList[-1]

    return newList

if __name__ == '__main__':
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("z-+.^."))
    print(solution("abcdefghijklmn.p"))