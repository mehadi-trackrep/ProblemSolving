class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = []
        max_len, substr_start_idx = 0, 0
        
        print("--> s: ", s)
        
        for curr_idx, char in enumerate(s):
            
            while char in char_set: ## here, we will search next valid substring start index
                char_set.pop(0)
                substr_start_idx += 1
            
            char_set.append(char)
            
            print("==> curr_idx: {}, c: {}, substr_start_idx: {}".format(
                    curr_idx,char,substr_start_idx
                )
            )
            max_len = max(  ## current index (curr_idx) is the sofar substring last index
                max_len, 
                curr_idx - substr_start_idx + 1
            )
        return max_len

if __name__ == '__main__':
    obj = Solution()
    s = 'abcaabcddefghh' ## defgh - 5
    '''
        a
        ab
        abc
        abca X
        bca
        ...
    '''
    s = 'aab'
    # s = 'dvdf'
    # s = 'abcaabcddh' ## defgh - 5
    print(obj.lengthOfLongestSubstring(s))