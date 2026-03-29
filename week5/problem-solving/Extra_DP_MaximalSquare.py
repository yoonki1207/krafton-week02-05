# DP - Maximal Square
# 문제 링크: https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        matrix = [list(map(int, row)) for row in matrix]
        row_arr = [[0] * m for _ in range(n)]
        col_arr = [[0] * m for _ in range(n)] 

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    if j == 0:
                        row_arr[i][j] = 1
                    else:
                        row_arr[i][j] = row_arr[i][j-1] + 1
                    if i == 0:
                        col_arr[i][j] = 1
                    else:
                        col_arr[i][j] = col_arr[i-1][j] + 1
        # dp = [[0] * m for _ in range(n)]
        # 만약 dp[i-1][j-1]이 길이 k의 정사각형을 이루고 있다면, 동시에 row_arr[i][j] >= k and col_arr[i][j] >= k라면, dp[i][j] = k + 1
        # for i in range(n):
        #     dp[i][0] = matrix[i][0]
        # for j in range(n):
        #     dp[0][j] = matrix[0][j]
        for i in range(1, n):
            for j in range(1, m):
                k = matrix[i-1][j-1]
                if k >= 1:
                    matrix[i][j] = min(k + 1, row_arr[i][j], col_arr[i][j])
        # print(matrix)
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, matrix[i][j])
        return ans * ans