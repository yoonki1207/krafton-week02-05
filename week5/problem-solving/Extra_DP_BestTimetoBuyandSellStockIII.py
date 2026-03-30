# DP - Best Time to Buy and Sell Stock III
# 문제 링크: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        arr = [0] * n
        brr = [0] * n
        m1 = prices[0]
        m2 = prices[n-1]
        k = 0
        for i in range(n):
            m1 = min(m1, prices[i])
            arr[i] = prices[i] - m1

            m2 = max(m2, prices[n-i-1])
            brr[n-i-1] = m2 - prices[n-i-1]
            if n-i < n:
                brr[n-i-1] = max(brr[n-i-1], brr[n-i])
            k = max(k, brr[n-i-1])
        # print(arr)
        # print(brr)
        # print(m1, m2)
        ans = 0
        for i in range(n-1):
            ans = max(ans, arr[i] + brr[i+1])
        return max(ans, k)
'''
3 3 5 0 0 3 1 4
0 0 2 0 0 3 0 4 - O(N) 해당 인덱스에서 팔았을 때의 최소값
이후의 최소값?
0 0 0 0 0 1 1 4
--- 해당 인덱스에서 샀을 때의 최대값
2 2 0 4 4 1 3 0
--- 해당 인덱스 이후에 샀을 때의 최대값
4 4 4 4 4 3 3 0



10000 C 4

30 + 30,
50

100 75 125 130 20 50


'''