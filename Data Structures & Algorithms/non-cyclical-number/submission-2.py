class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquaresOfDigit(n):
            total = 0
            while n:
                rem = n % 10
                total += rem ** 2
                n //= 10
            return total

        slow, fast = n, sumOfSquaresOfDigit(n)
        while slow != fast:
            fast = sumOfSquaresOfDigit(fast)
            fast = sumOfSquaresOfDigit(fast)
            slow = sumOfSquaresOfDigit(slow)
        return fast == 1
        