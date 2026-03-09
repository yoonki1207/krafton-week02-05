# 배열 - Candy
# 문제 링크: https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
from typing import List

# Solution
class Solution:
    def flush(self, v: List[int], base_candy) -> int:
        # print("Flush:", v, end='')
        n = len(v) - 1
        result = n * (n + 1) // 2
        result += max(n + 1, base_candy)
        # print(result)
        return result
    
    def candy(self, ratings: List[int]) -> int:
        ans = 0
        base_candy = 1
        stk = []
        for rate in ratings:
            # print(stk)
            if len(stk) == 0: 
                stk.append(rate)
            elif stk[-1] > rate:
                stk.append(rate)
            else:
                # flush
                # bigger,
                if stk[-1] < rate:
                    ans += self.flush(stk, base_candy)
                    if len(stk) == 1:
                        base_candy = base_candy + 1
                    else:
                        base_candy = 2
                    stk.clear()
                    stk.append(rate)
                    pass
                else : # same
                    ans += self.flush(stk, base_candy)
                    stk.clear()
                    stk.append(rate)
                    base_candy = 1
                    pass
                # same
            pass
        ans += self.flush(stk, base_candy)
        return ans
    


# Input Case
# solution = Solution()
# ratings = [1, 0, 2]
# print(solution.candy(ratings), "Expected: 5")
# ratings = [1, 2, 2]
# print(solution.candy(ratings), "Expected: 4")
# ratings = [1,3,2,2,1]
# print(solution.candy(ratings), "Expected: 7")
# ratings = [1,2,87,87,87,2,1]
# print(solution.candy(ratings), "Expected: 13")
# ratings = [1,2,3]
# print(solution.candy(ratings), "Expected: 6")
# ratings = [3,2,1]
# print(solution.candy(ratings), "Expected: 6")
# ratings = [0,1,2,5,3,2,7]
# print(solution.candy(ratings), "Expected: 15")
# ratings = [1,2,1,2,1]
# print(solution.candy(ratings), "Expected: 7")

# cases = [
#     ([1,0,2], 5),
#     ([1,2,2],4),
#     ([1,3,2,2,1],7),
#     ([1,2,87,87,87,2,1], 13),
#     ([1,2,3], 6),
#     ([3,2,1], 6),
#     ([0,1,2,5,3,2,7], 15)
# ]

# for ratings, output in cases:
#     if output != solution.candy(ratings):
#         print("Error: ", ratings, output)
