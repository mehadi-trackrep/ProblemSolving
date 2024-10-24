
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        idx = 0

        maxLen = a + b + c
        currA = currB = currC = 0 # tracing consecutive occurrance of a, b & c
        
        '''
            v.v.i. => if we have so far the ans string like - 'cc'
                        then for the next iteration we can take either 'a' / 'b' not 'c' cause currC == 2
                        
                        so, we can take 'a' and then we will have currA = 1. Now, we dont' need to remember the previous
                        'c' occurances right?
                        As, we started with a new character. That's why, we will make currC = 0 & currB = 0 as well.
        '''

        while idx < maxLen:
            
            # will will add single char in each iteration
            if (currA != 2 and a >= b and a >= c) or (a > 0 and (currB == 2 or currC == 2)):
                    ans += 'a'
                    currA += 1
                    currB = currC = 0 # reset
                    a -= 1
            elif (currB != 2 and b >= a and b >= c) or (b > 0 and (currA == 2 or currC == 2)):
                    ans += 'b'
                    currB += 1
                    currA = currC = 0 # reset
                    b -= 1
            elif (currC != 2 and c >= a and c >= b) or (c > 0 and (currA == 2 or currB == 2)):
                    ans += 'c'
                    currC += 1
                    currA = currB = 0 # reset
                    c -= 1

            idx += 1
            
        return ans

if __name__ == "__main__":
    obj = Solution()
    ans = obj.longestDiverseString(
        a = 0,
        b = 8,
        c = 11
    )
    print(ans)