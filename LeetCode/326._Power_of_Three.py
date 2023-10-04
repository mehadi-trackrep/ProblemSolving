class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        flag = False
        while n > 1:
            if n == 1:
                flag = True
            n /= 3
        return True if n == 1 or flag else False

class Solution: ## recursion -- JOSS!
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        if n <= 0 or n % 3 > 0: return False
        return self.isPowerOfThree(n/3)

if __name__ == '__main__':
    obj = Solution()
    assert obj.isPowerOfThree(27) == True
    assert obj.isPowerOfThree(1) == True
    assert obj.isPowerOfThree(-1) == False
    assert obj.isPowerOfThree(0) == False
    assert obj.isPowerOfThree(45) == False
    assert obj.isPowerOfThree(81) == True