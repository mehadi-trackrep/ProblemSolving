class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26 ## as input chars from English letters
        for idx in range(len(s)):
            freq[ord(s[idx]) - ord('a')] += 1
            freq[ord(t[idx]) - ord('a')] -= 1
        for val in freq:
            if val != 0:
                return False
        return True

    
if __name__ == "__main__":
    obj = Solution()
    s = ''
    t = ''
    print(obj.isAnagram(s, t))