'''
백준 문제 : 1932 (정수 삼각형)
DP Table = dp[i][j]에 저장된 값이 최대인 경우, 누적합을 통해 알 수 있습니다.
1. 큰 문제를 작게 생각
2. 작게 생각한 문제로 큰 문제를 해결
'''
import sys
n = int(sys.stdin.readline())
dp = []
for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0: # 맨 왼쪽의 경우
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif j == len(dp[i]) - 1: # 맨 오른쪽의 경우
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
print(max(dp[n-1]))
'''
    
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''