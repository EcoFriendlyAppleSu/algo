# for, if를 한번에
# list comprehension

def solution(mylist):
    answer = [ i**2 for i in mylist if i % 2 == 0]
    return answer

if __name__ == '__main__':
    mylist = [3,2,6,7]
    print(solution(mylist))