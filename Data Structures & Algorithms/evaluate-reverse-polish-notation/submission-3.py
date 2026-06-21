class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []
        for var in tokens:
            if var in ['+', '-', '*', '/']:
                var2 = int(stack.pop())
                var1 = int(stack.pop())
                if var == '+':
                    total = var1 + var2
                elif var == '-':
                    total = var1 - var2
                elif var == '*':
                    total = var1 * var2
                else:
                    total = int(var1 / var2)

                stack.append(total)
                    
            else:
                stack.append(var)

        return int(stack[-1])

                