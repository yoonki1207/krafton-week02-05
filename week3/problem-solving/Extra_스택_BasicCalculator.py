# 스택 - Basic Calculator
# 문제 링크: https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
NUMBERS = '0123456789'
class Solution:
    def calculate(self, s: str) -> int:
        # s = ''.join([i for i in s.split() if i != ''])
        stk = []
        n = len(s)
        i = 0
        # print(stk)
        while i < n:
            c = s[i]
            if c in NUMBERS:
                number_stack = []
                while i < n and s[i] in NUMBERS:
                    number_stack.append(s[i])
                    i += 1
                number = ''.join(number_stack)
                number = int(number)
                stk.append(number)                
                pass
            elif c in '+-()': # operation
                stk.append(c)
                i += 1
                pass
            else:
                i += 1

            # OPERATE
            if stk: # ), int
                if stk[-1] == ')':
                    stk.pop() # 무조건 숫자
                    number = stk.pop()
                    stk.pop() # 무조건 (
                    stk.append(number)
                    pass
                if type(stk[-1]) is int and len(stk) > 1:
                    while type(stk[-1]) is int and len(stk) > 1:
                        number = stk.pop()
                        if stk:
                            if stk[-1] == '-': # check unary or not
                                stk.pop()
                                if not stk or stk[-1] == '(': # use - as unary
                                    stk.append(-number)
                                else: # substract
                                    operand = stk.pop()
                                    stk.append(operand - number)
                            elif stk[-1] == '+': # add
                                stk.pop()
                                operand = stk.pop()
                                stk.append(number + operand)
                                pass
                            elif stk[-1] == '(':
                                stk.append(number)
                                break
                                pass
                            else:
                                break
                            pass
            pass
        return stk[0]
        pass

solution = Solution()
expr = '1 + 1'
expr = '(1+(4+5+2)-3)+(6+8)'
# expr = '2-1 + 2 '
print(solution.calculate(expr))
# size of s <= 300,000