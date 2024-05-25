
"""
    Solution link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
            1)  We will use sliding window technique to solve this problem.
                But the window size will be increased & decreased(shrinked) dynamically.
            
            Hack: When will the window be shrinked?
                    Ans: UniqueCharCount > maxUniqueCharCount_limit (loop 1 to maxUniqueCharCount)
            2)  We will calculate the substring length when 2 conditions statisfied:-
                    2.1. currentSubstringUniqueCharsCount == maxUniqueCharCount_limit for this iteration &
                    2.2. all of the chars freq >= k (in other syntax:-
                            * we will have a variable - k_conditionSatisfiedCharsCount = 0
                            when a char freq == k then we will just increase k_conditionSatisfiedCharsCount
                            then finally the condition is:-
                            k_conditionSatisfiedCharsCount == currentSubstringUniqueCharsCount
                        )
        """
        sz = len(s)
        max_len = 0
        window_start = window_end = 0
        totalUniqueCharCount = len(set(s))
        char_freq = [0 for _ in range(26)] # 0 to 25 index will be used for a (97) to z (122)

        for maxUniqueCharCountLimit in range(totalUniqueCharCount):
            for i in range(26): # clear
                char_freq[i] = 0
            currentUniqueCharsCount = k_conditionSatisfiedCharsCount = 0
            while (window_end < sz): # expanding or shrinking
                if currentUniqueCharsCount <= maxUniqueCharCountLimit: # expanding
                    """
                        We have to do 4 thinks here:-
                            1) calculate the current unique chars
                            2) increase the char frequency
                            3) calculate if we got the k_condition_satisfied char or not already
                            4) increase the window length
                    """
                    idx = ord(s[window_end]) - ord('a')
                    if char_freq[idx] == 0:
                        currentUniqueCharsCount += 1
                    char_freq[idx] += 1
                    if char_freq[idx] == k:
                        k_conditionSatisfiedCharsCount += 1
                    window_end += 1
                else: # shrinking
                    """
                        Here, the steps will be kinda reverse order
                    """
                    idx = ord(s[window_end]) - ord('a')
                    if char_freq[idx] == k:
                        k_conditionSatisfiedCharsCount -= 1
                    char_freq[idx] -= 1
                    if char_freq[idx] == 0:
                        currentUniqueCharsCount -= 1
                    window_start += 1

                # calculate the length
                if  currentUniqueCharsCount == maxUniqueCharCountLimit and \
                        currentUniqueCharsCount == k_conditionSatisfiedCharsCount:
                    max_len = max(max_len, window_end - window_start)
                
        return max_len