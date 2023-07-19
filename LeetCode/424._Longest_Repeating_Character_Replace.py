class Solution:
    def characterReplacement(self, s: str, k: int) -> int: ## TC: O(26*N)
        '''
            For each substring/window, we have a length windowlength & 
            we have a count in there most frequent character.
            So, if 
                    windowlength - count(most frequent char) <= k
                then this window is a valid window.
        '''
        l = 0
        length = len(s)
        freq = {}
        max_freq_char_len = 0
        max_valid_window_len = 0

        for r in range(length):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            max_freq_char_len = max(max_freq_char_len, freq[s[r]])
            while (r - l + 1) - max_freq_char_len > k: ## (r - l + 1) ==> current_window_length
                freq[s[l]] -= 1
                l += 1
            max_valid_window_len = max(max_valid_window_len, (r - l + 1))
        
        return max_valid_window_len
            
if __name__ == '__main__':
    obj = Solution()
    s = "ABABBA"
    k = 2
    # s = "AABABBA"
    # k = 1
    print(obj.characterReplacement(s, k))