# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

N = int(input())
dp = [0] * (N + 1)
if N <= 2:
    print(N)
    exit()
dp[0] = 1
a = 1
b = 1
c = 2
for i in range(2, N + 1):
    c = a + b
    c %= 15746
    b = a
    a = c
print(c)