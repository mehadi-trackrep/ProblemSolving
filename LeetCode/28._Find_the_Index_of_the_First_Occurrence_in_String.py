class Solution1:
    """
    Time Complexity: O(n * m) in worst case
    Space Complexity: O(1)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        idx = haystack.find(needle)
        return idx

class Solution:
    """
    Time Complexity: O(n * m)
        It will check at every index - idx for every substring of length m in the haystack
        So, upper loop upto n-m+1 and inner loop upto m; So, O(n * m)
    Space Complexity: O(1)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        lh, ln = len(haystack), len(needle)
        for idx in range(lh-ln+1):
            if haystack[idx:idx+ln] == needle:
                return idx
        return -1

if __name__=="__main__":
    obj = Solution()
    