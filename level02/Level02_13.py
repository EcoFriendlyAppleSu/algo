# 전화번호 목록

def solution(phone_book):
    answer = True
    sortedPhoneBook = sorted((phone_book), key=len)

    for i in range(len(sortedPhoneBook) -1):
        temp = sortedPhoneBook[i]
        if answer == False:
            break
        for j in range(i+1, len(sortedPhoneBook)):
            if temp[:len(temp)] == sortedPhoneBook[j][:len(temp)]:
                answer = False
                break
    return answer

# 더 파이썬다운 풀이법
# 만약에 어떤 번호가 다른 번호의 접두어라면 이 둘은 정렬했을 때 앞뒤에 위치하게 된다.!
def solution2(phone_book):
    answer = True
    sortedPhoneBook = sorted((phone_book))

    for p1, p2 in zip(sortedPhoneBook, phone_book[1:]):
        if p2.startswith(p1):
            answer = False
    return True

if __name__ == '__main__':
    # phoneBook = ["119", "97674223", "1195524421"]
    phoneBook = ["12","123","1235","567","88"]
    print(solution2(phoneBook))