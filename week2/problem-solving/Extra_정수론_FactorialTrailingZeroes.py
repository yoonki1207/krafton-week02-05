# 정수론 - Factorial Trailing Zeroes
# 문제 링크: https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt_5 = 0
        cnt_2 = 0
        for i in range(1, n+1):
            while i % 5 == 0:
                cnt_5 += 1
                i //= 5
            while i % 2 == 0:
                cnt_2 += 1
                i //= 2
        return min(cnt_5, cnt_2)