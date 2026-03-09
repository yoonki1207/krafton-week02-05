# 정수론 - Max Points on a Line
# 문제 링크: https://leetcode.com/problems/max-points-on-a-line/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    
    def gcd(self, a, b):
        if b == 0: return a
        return self.gcd(b, a%b)

    def maxPoints(self, points: List[List[int]]) -> int:
        gradients = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if dy < 0: # 항상 dy를 양수로
                    dx, dy = -dx, -dy
                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                g = self.gcd(abs(dy), abs(dx))
                if g != 0:
                    dy, dx = dy // g, dx // g
                # gradients.add((dy, dx))
                n = (dx * y1 - dy * x1)
                m = dx
                g = self.gcd(abs(n), abs(m))
                if g != 0:
                    n //= g
                    m //= g
                if n < 0: # n을 항상 양수로
                    n, m = -n, -m
                tu = (dy, dx, n, m)
                if dx == 0:
                    tu = (dy, dx, x1, 0)
                elif dy == 0:
                    tu = (dy, dx, y1, 0)
                # print(n, m)
                if tu not in gradients:
                    gradients[tu] = 0
        # print(gradients)
        # return max(gradients.values())
        elements = list(gradients.copy())
        # print(elements)
        # print("points:", points)
        for x, y in points:
            # print()
            # print("P:", x,  y)
            for element in elements:
                # print("for element:", element)
                dy, dx, n, m = element
                if dx == 0:
                    if x == n:
                        # print('vertical',x, y)
                        gradients[element] += 1
                        # print('',gradients[element])
                elif dy == 0:
                    if y == n:
                        # print('horizontal',x, y)
                        gradients[element] += 1
                elif y * dx * m == (dy * x * m + dx * n):
                    gradients[element] += 1
        # print(gradients)
        if len(points) == 1: return 1
        return max(gradients.values())

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
