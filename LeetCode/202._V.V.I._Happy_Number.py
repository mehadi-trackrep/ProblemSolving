class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sum_of_squared_digits(n)
        # if n == 1:
        #     return True
        while fast != 1 and slow != fast:
            slow = self.sum_of_squared_digits(slow)
            fast = self.sum_of_squared_digits(self.sum_of_squared_digits(fast))
        if fast == 1:
            return True
        return False
    def sum_of_squared_digits(self, n):
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n //= 10
        return sum