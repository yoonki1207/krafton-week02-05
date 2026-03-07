# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
T = int(input())
for test_case in range(T):
    s = input().split()
    n = int(s[0])
    scores = list(map(int, s[1:]))
    avg = sum(scores) / n
    above_avg_n = 0
    for i in scores:
        if i > avg:
            above_avg_n += 1
    result = above_avg_n/n*100
    print(f"{result:.3f}%")