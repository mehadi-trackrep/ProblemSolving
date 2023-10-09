class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        counter = 1 # "1" means still valid window; "0" means now the window has been invalid
        mx_length_window = 0
        mp = {}

        while end < len(s):
            mp[s[end]] = mp.get(s[end], 0) + 1
            if mp[s[end]] > 1:
                counter = 0
            
            while counter == 0:
                mp[s[start]] -= 1
                if mp[s[start]] == 1:
                    counter = 1
                start += 1

            mx_length_window = max(mx_length_window, end - start + 1)
            
            end += 1
        
        return mx_length_window

if __name__ == '__main__':
    obj = Solution()