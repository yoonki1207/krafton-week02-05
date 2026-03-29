# DP - Longest Increasing Subsequence
# 문제 링크: https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def lowerbound(self, arr, val):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def lengthOfLIS(self, nums: List[int]) -> int:
        v = []
        for n in nums:
            if not v: v.append(n)
            elif v[-1] < n:
                v.append(n)
                pass
            else:
                index = self.lowerbound(v, n)
                v[index] = n
        return len(v)
                