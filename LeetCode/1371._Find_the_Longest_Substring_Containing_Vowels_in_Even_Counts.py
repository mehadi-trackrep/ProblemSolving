class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
            #Intuition
            Here, we don't store the count/occurances rather than we will just save the 
            occurance of a vowel is even or not.
            We have total 5 vowels - a,e,i,o,u.
            So, we can use bitmask with 5 bits on and off.
                For an index - i, we might have multiple bits on which means all of the corresponding vowels occurred
            at odd times other bits 0 means they have occurred even times including 0 occurrences.
            

            #Approach
            1)Track Vowel Occurrences Using Bitmasking:
            We initialize a bitmask (mask) with 5 bits, each corresponding to a vowel.
            As we traverse the string, we update the bitmask based on the vowel we encounter. For instance, if we encounter an 'a', we flip the 0th bit; if it's 'e', we flip the 1st bit, and so on.
            
            2)Map to Track Previous Occurrences:
            We use a hash map (m) to store the first occurrence of each bitmask value.
            If the current bitmask has been seen before, it means the substring between the previous occurrence and the current position contains an even number of each vowel, so we calculate the length of this substring.
            
            3)Initial Condition:
            We initialize the bitmask 0 in the map at index -1 because a bitmask of 0 means all vowels have appeared an even number of times. This helps when we find such a substring starting from the beginning.
            
            4)Return the Maximum Length:
            As we process the string, we keep track of the maximum length of the valid substrings where all vowels appear an even number of times.
        
        Ref: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/?envType=daily-question&envId=2024-09-15
        """
        n = len(s)
        mask = 0
        maxLength = 0
        m = {0: -1}
        
        # print("==> input string: s - ",s)
        
        for i in range(n):
            if s[i] == 'a':
                mask ^= (1 << 0) # mask ^= 1 (from last do 1st bit on)
            elif s[i] == 'e':
                mask ^= (1 << 1) # mask ^= 2 (from last, do 2nd bit on)
            elif s[i] == 'i':
                mask ^= (1 << 2) # mask ^= 4 (from last, do 3rd bit on)
            elif s[i] == 'o':
                mask ^= (1 << 3) # mask ^= 8 (from last, do 4rth bit on)
            elif s[i] == 'u':
                mask ^= (1 << 4) # mask ^= 16 (from last, do 5th bit on)
            
            # print(f"mask: {mask}, s[i]: {s[i]}")
            
            if mask in m:
                # print(f"\t#map, m: {m}")
                # print(f"\t#maxLength: {maxLength}, i - m[mask]: {i - m[mask]}")
                maxLength = max(maxLength, i - m[mask])
            else:
                # print(f"[else], i: {i}\n")
                m[mask] = i
        
        return maxLength
    
if __name__=="__main__":
    obj = Solution()
    # print(obj.findTheLongestSubstring(s="elee")) # 3
    print(obj.findTheLongestSubstring(s="eleetcodo")) # 11
    print("\t\t\t\t======\t\t\t\t\t\n")
    print(obj.findTheLongestSubstring(s="eleetcodoe")) # 11
    # print(obj.findTheLongestSubstring(s="eleetcodeouppsgreateat")) # 11
    
    # print(obj.findTheLongestSubstring(s="eleetcodeoppsgreateat")) # 21