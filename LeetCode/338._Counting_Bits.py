from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
1 - 01 - 1 (2^0)
2 - 10 - 1 1 (2^1)
3 - 11 - 1
4 - 100 = 1 1 (2^2)

5 - 101 = 2 (4+1)
6 - 110 = 2 (4+2)
7 - 111 = 3 (4+3)
8 - 1000 = 1 1 (2^3)

9 - 1001 = 2 (8+1
10 - 1010 = 2 (8+2)
11 - 1011 = 3 (8+3)
12 - 1100 = 2 (8+4)
13 - 1101 = 3 (8+5)
14 - 1110 = 3 (8+6)
15 - 1111 = 4 (8+7)
16 - 10000 = 1 1 (2^4)

17 - (16+1)
18 - (16+2)

[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2]

        """
        if n == 0:
            return [0]
        elif n == 1:
            return [0,1]
        elif n == 2:
            return [0,1,1]
        elif n == 3:
            return [0,1,1,2]
        
        ans = [0,1,1,2,1]
        power_of_two_val = 4 # 2, 4, 8, 16, 32, 64, 128, ...
        for i in range(5, n+1): # 5 to n
            if i == 2 * power_of_two_val:
                power_of_two_val *= 2
                ans.append(1)
            else:
                ans.append(1 + ans[i - power_of_two_val])

        return ans

"""
    Same things basically, but more concise maybe
    for(int i = 1; i <= n; ++i)
            t[i] = t[i >> 1] + i % 2;
Analysis
    To understand the solution, we remember the following two points from math:

    All whole numbers can be represented by 2N (even) and 2N+1 (odd).
    For a given binary number, multiplying by 2 is the same as adding a zero at 
    the end (just as we just add a zero when multiplying by ten in base 10).
    Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's. Likewise, doubling a number and adding one will increase the count by exactly 1. Or:

    countBits(N) = countBits(2N)
    countBits(N)+1 = countBits(2N+1)

    Thus we can see that any number will have the same bit count as half that number, with an extra one if it's an odd number. We iterate through the range of numbers and calculate each bit count successively in this manner:

    for i in range(num):
        counter[i] = counter[i // 2] + i % 2
    
    With a few modifications:
        Define the base case of counter[0] = 0, and start at 1.
        We need to include num, so use num+1 as the bound on the range.
        Bit-shifting 1 has the same effect as dividing by 2, and is faster, so replace i // 2 
        with i >> 1.
        We can choose to either initiate our list with counter = [0] * (num+1) or just 
        counter = [0] and then append to it (which has O(1)). It's a little faster to initiate 
        it with zeroes and then access it rather than appending each time, but I've chosen the 
        latter for better readibility.
        Some solutions use i & 1 to determine the parity of i. While this accomplishes the same 
        purpose as i % 2 and keeps with the bitwise-operator theme, it is faster to calculate 
        the modulus.

"""

if __name__ == '__main__':
    obj = Solution()
    print(obj.countBits(n=2))
    print(obj.countBits(n=5))
    print(obj.countBits(n=17))
    print(obj.countBits(n=16))