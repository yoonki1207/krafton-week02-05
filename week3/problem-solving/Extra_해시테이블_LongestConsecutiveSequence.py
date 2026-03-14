# 해시 테이블 - Longest Consecutive Sequence
# 문제 링크: https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            s.add(i)
        ans = 0
        for i in nums:
            if i in s:
                s.remove(i)
                cnt = 1
                j = i + 1
                while j in s:
                    s.remove(j)
                    j += 1
                    cnt += 1
                    pass
                j = i - 1
                while j in s:
                    s.remove(j)
                    j -= 1
                    cnt += 1
                    pass
                ans = max(ans, cnt)
            pass
        return ans
        
# solution = Solution()
# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = []
# result = solution.longestConsecutive(nums)
# print(result)