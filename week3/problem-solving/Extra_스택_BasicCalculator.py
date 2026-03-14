# 스택 - Basic Calculator
# 문제 링크: https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
NUMBERS = '0123456789'
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '+':
                result += sign*num
                num = 0
                sign = 1
            elif c == '-':
                result += sign*num
                num = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += sign*num
                num = 0
                result *= stack.pop()
                result += stack.pop()
        
        return result + sign*num

solution = Solution()
expr = '1 + 1'
expr = '(1+(4+5+2)-3)+(6+8)'
# expr = '2-1 + 2 '
print(solution.calculate(expr))
# size of s <= 300,000