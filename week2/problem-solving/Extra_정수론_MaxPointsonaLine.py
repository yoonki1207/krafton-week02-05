# 정수론 - Max Points on a Line
# 문제 링크: https://leetcode.com/problems/max-points-on-a-line/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    
    def gcd(self, a, b):
        if b == 0: return a
        return self.gcd(b, a%b)

    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        for i in range(len(points)):
            gradients = {}
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0:
                    dy = 1
                if dy == 0:
                    dx = 1
                if dx != 0 and dy != 0:
                    g = self.gcd(abs(dy), abs(dx))
                    dy, dx = dy // g , dx // g
                if dy < 0:
                    dy, dx = -dy, -dx
                tu = (dy, dx)
                if tu in gradients:
                    gradients[tu] += 1
                else:
                    gradients[tu] = 1
            if len(gradients) > 0:
                ans = max(ans, max(gradients.values()) + 1)
        return ans

solution = Solution()
# points = [[1,1],[2,2],[3,3]]
# output = 3
# print(solution.maxPoints(points))
# points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# output = 4
# print(solution.maxPoints(points))

# points = [[0, 0]]
# output = 1
# print(solution.maxPoints(points))

# points = [[0, 1], [0, 0]]
# output = 2
# print(solution.maxPoints(points))

# points = [[3,3],[1,4],[1,1],[2,1],[2,2]]
# output = 3
# print(solution.maxPoints(points))

points = [[2,3],[3,3],[-5,3]]
output = 3
print(solution.maxPoints(points))

points = [[3,2],[3,3],[3,-5]]
output = 3
print(solution.maxPoints(points))
