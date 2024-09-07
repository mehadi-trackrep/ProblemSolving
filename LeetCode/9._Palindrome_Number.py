class Solution:
    def isPalindrome(self, x: int) -> bool:
        xx = x
        ix = 0
        if x < 0:
            return False
        while xx:
            r = xx % 10
            xx //= 10
            ix = ix * 10 + r
        
        return True if x == ix else False
        