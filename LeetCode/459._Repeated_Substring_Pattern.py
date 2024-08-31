class Solution1:
    """
        If there is a substring then at least it should be repeated twice.
        Meaning that if the output is True then the input string length is even and at least 
        twice of the substirng.
        Hacks:-
            input string - S
                S1 = S + S
                S2 = S[1:] + S[:len(S)-1]
                If S has a substring like ss then S = ss * n times
                So, in the S2, there should be the original input string (S).
    """
    def repeatedSubstringPattern(self, s: str) -> bool:
        ln = len(s)
        s1 = s + s
        s2 = s[1:] + s[:ln-1]
        return True if s in s2 else False

class Solution:
    """
        If there is a substring then at least it should be repeated twice.
        So, we can check the substring from 1 to len(s)//2.
        And obviously the input string should be even if it has a repeated substring.
        Furthermore, the repeated substring length will be divisible by the input string length.
        So, for every iteration, we can if the index is divisible by the input string length.
            If yes then we have to check, is it possible to get the input string by repeating the substring.
            
        For example:-
            s = "abcabc"
            ln = 6
            for i in range(1, 6//2+1):
                i = 1
                    6 % i != 0
                i = 2
                    6 % i = 0
                    s[0:i] = s[0:2] = ab
                    s[0:i]*(6//i) = ab*3 = ababab
                    s = abcabc
                    s[0:i]*(6//i) != s
                i = 3
                    6 % i = 0
                    s[0:i] = s[0:3] = abc
                    s[0:i]*(6//i) = abc*2 = abcabc
                    s = abcabc
                    s[0:i]*(6//i) == s
                    return True
    """
    
    def repeatedSubstringPattern(self, s: str) -> bool:
        ln = len(s)
        for i in range(1, ln//2+1):
            if ln % i == 0:
                if s[0:i]*(ln//i) == s: return True
        return False
    
        
if __name__=="__main__":
    obj = Solution()
    print(obj.repeatedSubstringPattern("abab")) # True
    print(obj.repeatedSubstringPattern("aba")) # False
    print(obj.repeatedSubstringPattern("abcabcabcabc")) # True
    print(obj.repeatedSubstringPattern("abcabcdabcabcd")) # True
    print(obj.repeatedSubstringPattern("abcabcdabcabcc")) # False