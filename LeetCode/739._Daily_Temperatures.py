from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        answer = []
        
        ln = len(temperatures)
        
        for idx in range(ln-1, -1, -1):
            cur = temperatures[idx]
            isFound = False

            while stack and not isFound:
                if stack[::-1][0][0] > cur:
                    answer.append(stack[::-1][0][1] - idx)
                    stack.append((cur, idx))
                    isFound = True
                else:
                    _ = stack.pop()

            if not stack:
                answer.append(0)
                stack.append((cur, idx))
        
        return answer[::-1]