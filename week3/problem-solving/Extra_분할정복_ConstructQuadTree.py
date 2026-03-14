# 분할정복 - Construct Quad Tree
# 문제 링크: https://leetcode.com/problems/construct-quad-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a QuadTree node.
from typing import List
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def getColor(self, y, x, m, grid: List[List[int]]):
        ret = 0
        for i in range(y, y + m):
            for j in range(x, x + m):
                ret += grid[i][j]
        if ret == m*m:
            return 1
        elif ret == 0:
            return 0
        return -1
    def construct_help(self, y, x, m, grid: List[List[int]]) -> 'Node':
        color = self.getColor(y, x, m, grid)
        if color >= 0:
            return Node(color, True, None, None, None, None)
        else:
            n = m//2
            return Node(1, False, 
                self.construct_help(y, x, n, grid), 
                self.construct_help(y, x+n, n, grid), 
                self.construct_help(y+n, x, n, grid), 
                self.construct_help(y+n, x+n, n, grid))
            pass

        pass
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.construct_help(0, 0, len(grid), grid)
        pass