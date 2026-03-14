# 해시 테이블 - Longest Consecutive Sequence
# 문제 링크: https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for n in s:
            if n-1 not in s:
                cnt = 1
                while n + cnt in s:
                    cnt += 1
                ans = max(ans, cnt)
        return ans
        
solution = Solution()
nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
nums = []
result = solution.longestConsecutive(nums)
print(result)