class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += 1
            n = n & (n-1)
        return cnt

if __name__ == '__main__':
    obj = Solution()
    ## the following values are the binary representation of the given decimal values - 11, 128
    ## N.B. If we do 2's complement then we will have same value but in signed, i mean in negative.
    assert obj.hammingWeight(0b00000000000000000000000000001011) == 3
    assert obj.hammingWeight(0b00000000000000000000000010000000) == 1