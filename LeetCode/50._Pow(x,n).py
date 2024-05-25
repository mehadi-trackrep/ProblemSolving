class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n) -> float:
            if n == 0:
                return 1
            if x == 0:
                return 0
            ans = rec(x*x, n//2) # 2^8 = (2*2)^4 = (2^2)^4
            return x * ans if n&1 else ans

        return rec(x, n) if n >= 0 else 1 / rec(x, -n)

if __name__ == '__main__':
    obj = Solution()
    assert obj.myPow(2.00000, 10) == 1024.00000
    assert obj.myPow(2.00000, -2) == 0.25000