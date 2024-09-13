from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        cur_score = 0
        mx_score = 0
        tokens.sort()
        ln = len(tokens)
        l, r = 0, ln-1
        
        while l <= r:
            if power >= tokens[l]: # face up
                power -= tokens[l]
                l += 1
                cur_score += 1
                mx_score = max(mx_score, cur_score)
            elif cur_score: # face down
                power += tokens[r]
                r -= 1
                cur_score -= 1
            else: break
        
        return mx_score
    
    
    
if __name__=="__main__":
    obj = Solution()
    print(obj.bagOfTokensScore(tokens=[200, 100], power=150))