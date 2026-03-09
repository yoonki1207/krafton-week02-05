# 백트래킹 - Word Search
# 문제 링크: https://leetcode.com/problems/word-search/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def dfs(self, y: int, x: int, board: List[List[str]], 
        visited: List[List[bool]],
        index: int,
        word: str) -> bool:
        if index >= len(word): return True
        for offset_y, offset_x in self.offsets:
            i = y + offset_y
            j = x + offset_x
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) :
                continue
            letter = board[i][j]
            if not visited[i][j] and letter == word[index]:
                visited[i][j] = True
                ret = self.dfs(i, j, board, visited, index + 1, word)
                visited[i][j] = False
                if ret: return True
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.dfs(i, j, board, visited, 1, word): return True
                    visited[i][j] = False

        return False

# solution = Solution()
# print(solution.exist([['a', 'b'], ['c', 'd']], 'abcd'))
# print(solution.exist([['a', 'b'], ['c', 'd']], 'abdc'))
# print(solution.exist([['a']], 'a'))
# print(solution.exist([['a', 'a']], 'aaa'))
