class Solution1:
    def evalRPN(self, tokens: list[str]) -> int: ## TC: O(n), SC: O(n)
        stack = []
        for token in tokens:
            if token in "+-*/":
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack.pop()

class Solution:
    def evalRPN(self, tokens: list[str]) -> int: ## TC: O(n), SC: O(1)
        '''
            Here, we will not use any auxiliary space.
            So, we have to use somehow the input tokens list! :D
        '''
        top = 0
        for token in tokens:
            if token in "+-*/":
                opd2, opd1 = int(tokens[top - 1]), int(tokens[top - 2])

                if token == "+":
                    tokens[top-2] = opd1 + opd2
                elif token == "-":
                    tokens[top-2] = opd1 - opd2
                elif token == "*":
                    tokens[top-2] = opd1 * opd2
                else:
                    tokens[top-2] = int(opd1 / opd2)
                top -= 1
            else:
                tokens[top] = token
                top += 1
        return int(tokens[top - 1])

if __name__ == '__main__':
    obj = Solution()

    assert obj.evalRPN(["18"]) == 18
    assert obj.evalRPN(["2","1","+","3","*"]) == 9
    assert obj.evalRPN(["4","13","5","/","+"]) == 6
    assert obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22