# 1이 될 때까지

def solution():
    N, K = map(int, input().split())
    count = 0
    while True:
        if (N % K) == 0:
            N //= K
            count += 1
        else:
            N -= 1
            count +=1

        if N == 1:
            break
    return count

if __name__ == '__main__':
    print(solution())
