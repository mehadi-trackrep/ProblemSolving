from collections import deque

class Solution1:
    def isValid(self, s: str) -> bool:
        l = len(s)
        stack = deque()
        for i in range(l):
            ch = s[i]
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if ch == ')' and top != '(':
                    return False
                if ch == ']' and top != '[':
                    return False
                if ch == '}' and top != '{':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        d = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in d.values():
                stack.append(ch)
            elif ch in d.keys():
                if len(stack) == 0 or stack.pop() != d[ch]:
                    return False
            else:
                return False
        return len(stack) == 0

if __name__ == '__main__':
    obj = Solution()

    assert obj.isValid("()")==True
    assert obj.isValid("()[]{}")==True
    assert obj.isValid("(]")==False