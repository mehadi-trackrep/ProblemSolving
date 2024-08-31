from typing import List

class Solution:

    def is_valid_string(self, word: str, vowels="aeiou") -> bool:
        if (word[0] in vowels) and (word[::-1][0] in vowels):
            return True
        return False

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        ln = len(words)
        prefixSum = [0 for _ in range(ln)]
        
        if self.is_valid_string(words[0]):
                prefixSum[0] = 1

        for i in range(1, ln):
            if self.is_valid_string(words[i]):
                prefixSum[i] = prefixSum[i-1] + 1
            else:
                prefixSum[i] = prefixSum[i-1]

        qln = len(queries)
        ans = []

        # print("==> prefixSum: ", prefixSum)

        for i in range(qln):
            l = queries[i][0]
            r = queries[i][1]

            # print("--> prefixSum[r] - prefixSum[l]: ", (prefixSum[r] - prefixSum[l]))
            # print("==> extra addition val: ", 1 if self.is_valid_string(words[l]) else 0)
            
            extra_val = 1 if self.is_valid_string(words[l]) else 0
            ans.append((prefixSum[r] - prefixSum[l]) + extra_val)

        return ans
    
if __name__ == "__main__":
    s = Solution()
    words = ["aba","bcb","ece","aa","e"]
    queries = [[0,2],[1,4],[1,1]]
    print(s.vowelStrings(words, queries)) # [2,3,0]