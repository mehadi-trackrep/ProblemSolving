class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        i, j = 0, 0
        while i < s_len and j < t_len:
            if s[i] == t[j]:
                print("i, j: {}, {}".format(i, j))
                i += 1
                j += 1
            else:
                j += 1
        if i >= s_len:
            return True
        else:
            return False
"""
    Two pointers just refers to using two integer variables 
    to move along some iterables. The strategies we looked at 
    in this article are the most common patterns, but always 
    be on the lookout for a different way to approach a problem.
"""
if __name__ == '__main__':  ## AC (Two pointers)
    obj = Solution()
    res = obj.isSubsequence(
        s='abc',
        t='ahbgdc'
    )
    print(res)

    