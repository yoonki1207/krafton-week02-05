# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

N, K = map(int, input().split()) 
arr = [0] * N
for i in range(N):
    w, v = map(int, input().split())
    arr[i] = (w, v)

dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        if j - arr[i-1][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1][0]]+arr[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])