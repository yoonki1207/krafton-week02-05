# DP - Longest Palindromic Substring
# 문제 링크: https://leetcode.com/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        ans = 1
        ans_s = s[0]
        N = len(s)
        for start_index in range(len(s)):
            left = start_index - 1
            right = start_index + 1
            cnt = 1
            while left >= 0 and right < N:
                if s[left] == s[right]:
                    cnt += 2
                else:
                    break
                left -= 1
                right += 1
            # ans = max(ans, cnt)
            if ans < cnt:
                ans_s = s[left+1:right]
                ans = cnt
            left = start_index
            right = start_index + 1
            if right >= N or s[left] != s[right]: continue
            cnt = 0
            while left >= 0 and right < N:
                if s[left] == s[right]:
                    cnt += 2
                else:
                    break
                left -= 1
                right += 1
            # ans = max(ans, cnt)
            if ans < cnt:
                ans_s = s[left+1:right]
                ans = cnt
        return ans_s