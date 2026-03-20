# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

n, k = map(int, input().split())
arr = set()
for i in range(n):
    a = int(input())
    if a <= k:
        arr.add(a)
    pass
arr = list(arr)
arr.sort(reverse=True)
INF = 987654321
ans = INF

from collections import deque

dp = [-1] * (k + 1)
dp[0] = 0

q = deque([0])

while q:
    curr = q.popleft()
    
    for coin in arr:
        n = curr + coin
        if n > k:
            continue
        if dp[n] != -1:
            continue
        dp[n] = dp[curr] + 1

        if n == k:
            print(dp[n])
            exit()
        q.append(n)

# dfs(arr, 0, k, 0)
if ans == INF:
    print(-1)
else:
    print(ans)

'''
BFS + memozation 을 이용한 문제
결국 DP문제이다.

0원을 만들기 위해 필요한 동전은 0개.
0에 대해서 동전 1개를 추가해 만들 수 있는 화폐는 a_0, a_1, ... 이다.
a_0에 대해서 동전 1개를 추가해 만들 수 있는 화폐는 a_0+a_0, a_0+a_1 ... 이다.
반복한다.

'''