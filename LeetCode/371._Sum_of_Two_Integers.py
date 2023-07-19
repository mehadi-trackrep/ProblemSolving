import math

class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while b:
            sum = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sum
            b = carry

        if (a>>31) & 1: # If a is negative in 32 bits sense
            return ~(a^mask)
        return a

class Solution_1:
    def getSum(self, a: int, b: int) -> int:
        '''
            We know, logB(m * n) = logBm + logBn
            Now, if B = e then
            loge(e^a * e^b) = loge(e^a) + loge(e^b)
                            = a * loge e + b * loge e
                            = a * 1 + b * 1
                            = a + b
            So,
            ln(expa∗expb)=ln(expa)+ln(expb)=a(ln(exp))+b(ln(exp))=a+b
        '''
        return int(math.log(math.exp(a) * math.exp(b))) if a!=0 and b!=0 else a or b
