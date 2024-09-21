from collections import defaultdict

class Solution:
    def checkFreqSame(self, mp1, mp2) -> bool:
        for i in range(26): # we have to check exactly the window (mp2) has same characters with same frequency
                                # not extra characters or extra/less frequency
            if mp1[i] != mp2[i]: return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
            Very good resource: https://leetcode.com/problems/permutation-in-string/solutions/1762469/c-sliding-window-optimized-well-explained/
            
        """
        ln1 = len(s1)
        ln2 = len(s2)
        
        mp1, mp2 = defaultdict(int), defaultdict(int)
        
        for char in s1:
            mp1[ord(char) - ord('a')] += 1
        
        i, j = 0, 0
        
        while j < ln2:
            mp2[ord(s2[j]) - ord('a')] += 1
            
            if j-i+1 == ln1: # current window length == len(s1)
                if self.checkFreqSame(mp1, mp2): return True
            if j-i+1 >= ln1:
                mp2[ord(s2[i]) - ord('a')] -= 1
                i += 1
            
            j += 1 # j++ means always the ending border shifted forward where start pointer might be in same 
                        # position if yes, the it just increases the window size
                        # otherwise, it shifts the window one step forward.
            
        return False