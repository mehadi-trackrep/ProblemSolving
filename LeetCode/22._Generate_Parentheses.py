from typing import List

class Solution:
    """
        We have to use backtrack. We have to take a item in stack and trying to go all possible directions and
        finally pop the item on the current function state, execute rest of the logic.
        
        N.B. if the number of sofar taken open paranthesis == n(closed) == n then push the stack items into result
        array.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(nOpenedParenthesis, nClosedParanthesis):
            if nOpenedParenthesis == nClosedParanthesis == n: # base case
                result.append("".join(stack))
                return
            if nOpenedParenthesis < n: # 2nd logic based on serial
                stack.append("(")
                backtrack(nOpenedParenthesis + 1, nClosedParanthesis)
                stack.pop()
            if nClosedParanthesis < nOpenedParenthesis:
                stack.append(")") # 3rd logic
                backtrack(nOpenedParenthesis, nClosedParanthesis + 1)
                stack.pop()
            return
        
        backtrack(0, 0)
        
        return result