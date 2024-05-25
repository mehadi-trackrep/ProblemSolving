class Solution1:
    def validPalindrome(self, s: str) -> bool:
        sz = len(s)
        flag = False
        l, r = 0, sz - 1
        while l < r:
            if s[l] != s[r]: # maximum one time mismatch allowed only
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            l += 1
            r -= 1
        return True
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r-= 1
        return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                delete_l_str = s[l+1:r+1] # excluding lth index
                delete_r_str = s[l:r] # excluding rth index
                return delete_l_str == delete_l_str[::-1] or delete_r_str == delete_r_str[::-1]
            l, r = l+1, r-1
        
        return True

obj = Solution()
print(obj.validPalindrome("aba"))
print(obj.validPalindrome("ababda"))
print(obj.validPalindrome("abac"))
print(obj.validPalindrome("abc"))
print(obj.validPalindrome("abcdedadedecba"))
print(obj.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))