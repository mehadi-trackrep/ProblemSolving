class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ln = len(s)
        total_palin_substrs = 0

        for i in range(self.ln):
            total_pal_substrs_from_ith_center = self.expandPalindromeWithIthCenter(s, i, i)
            total_pal_substrs_from_ith_i1th_center = self.expandPalindromeWithIthCenter(s, i, i+1)
            total_palin_substrs += (total_pal_substrs_from_ith_center + total_pal_substrs_from_ith_i1th_center)
        
        return total_palin_substrs 

    def expandPalindromeWithIthCenter(self, s, left, right) -> int: # found total palindromic substrings
        sofar_found_palindromic_substrings = 0
        
        while (left>=0 and right<self.ln) and (s[left] == s[right]):
            left -= 1
            right += 1
            sofar_found_palindromic_substrings += 1
        
        return sofar_found_palindromic_substrings
        

if __name__=="__main__":
    obj = Solution()
    print(obj.countSubstrings("abc"))
    print(obj.countSubstrings("aaa"))