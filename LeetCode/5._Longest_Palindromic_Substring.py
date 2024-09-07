class Solution:
    """
        Ref:
        ---
            1. https://leetcode.com/problems/longest-palindromic-substring/solutions/5676537/longest-palindromic-substring-an-easy-explaination/
            2. https://leetcode.com/problems/longest-palindromic-substring/solutions/4212564/beats-96-49-5-different-approaches-brute-force-eac-dp-ma-recursion/


        Intuition:
            - The obvious brute force solution is to pick all possible starting and ending positions for a 
            substring, and verify if it is a palindrome. There are a total of n^2 such substrings (excluding 
            the trivial solution where a character itself is a palindrome). Since verifying each substring takes
            O(n) time, the run time complexity is O(n^3).
        
        ## Two pointers:-
        Basically, we will iterate through the input string index by index and
            for each index we will try to find two palindromes like
                i) odd where ith index char will be the middle one
                ii) even where ith index char will be the 1st middle and (i+1)th char will be the 2nd middle.
            & then determine the max length and start, end.
            
            T.C. - O(n^2) # will try to find all possible palindromes
            But approach is two pointers
    """
    def longestPalindrome(self, s: str) -> str:
        '''
            Constraints:
                1 <= s.length <= 1000
                s consist of only digits and English letters.
        '''
        start, end = 0, 0 # targeted max palindrome substring start and end indices
        ln = len(s)
        self.ln = ln
        
        for i in range(ln):
            odd_len  = self.expandPalindromeStrFromCenter_i(s, i, i) # odd length palindromic substring search
            even_len = self.expandPalindromeStrFromCenter_i(s, i, i+1) # even length palindromic substring search
            
            new_ln = max(odd_len, even_len)
            
            if new_ln > (end - start):
                start = i - (new_ln - 1)//2 # it will work for odd / even length substring
                end = i + new_ln // 2 # same as
        
        # print(f"start, end; {start}, {end}")
        return s[start: end+1]
            
    def expandPalindromeStrFromCenter_i(self, s, left, right) -> int:
        while left >= 0 and right < self.ln and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1 # after being invalid the left and right already have been expanded!
    
class Solution1:
    # Two pointers

    def longestPalindrome(self, s: str) -> str:
        '''
            Constraints:
                1 <= s.length <= 1000
                s consist of only digits and English letters.
        '''
        start, end = 0, 0 # targeted max palindrome substring start and end indices
        self.ln = len(s)
        max_str = s[0]
        
        for i in range(self.ln):
            odd_str  = self.expandPalindromeStrFromCenter_i(s, i, i) # odd length palindromic substring search
            even_str = self.expandPalindromeStrFromCenter_i(s, i, i+1) # even length palindromic substring search
            
            if len(odd_str) > len(max_str):
                max_str = odd_str
            if len(even_str) > len(max_str):
                max_str = even_str
        
        return max_str
            
    def expandPalindromeStrFromCenter_i(self, s, left, right) -> str:
        while left >= 0 and right < self.ln and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right] # after being invalid the left and right already have been expanded!

if __name__=="__main__":
    obj = Solution()
    print(obj.longestPalindrome("babad"))
    print(obj.longestPalindrome("aaaa"))
    
    obj1 = Solution1()
    # print(obj1.longestPalindrome("babad"))
    print(obj1.longestPalindrome("aaaa"))
    