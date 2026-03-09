# 배열 - H-Index
# 문제 링크: https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def hable(self, citations: List[int], val: int):
        left = 0
        right = len(citations)
        last_left = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] < val:
                left = mid + 1
            elif citations[mid] >= val:
                last_left = mid
                right = mid - 1
        return len(citations) - last_left >= val
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        left = 0
        right = citations[-1]
        last_left = 0
        while left <= right:
            mid = (left + right) // 2
            if self.hable(citations, mid):
                last_left = mid
                left = mid + 1
            else:
                right = mid - 1
        return last_left
        

# solution = Solution()
# print(solution.hIndex([3, 0, 6, 1, 5]), "Expected 3")
# print(solution.hIndex([1, 3, 1]), "Expected 1")
# print(solution.hIndex([7, 2, 1 , 1, 1]), "Expected 2")
# print(solution.hIndex([3,3,3]), "Expected 3")