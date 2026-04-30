class Solution:
    def sumSquaresDigits(self, n: int) -> int:
        sum_squares_digits = 0
        while n > 0:
            sum_squares_digits += (n % 10) ** 2
            n //= 10
        return sum_squares_digits

    def isHappy(self, n: int) -> bool:
        # T: O(N) | S: O(1)
        slow = n
        fast = self.sumSquaresDigits(n)
        while slow != fast:
            slow = self.sumSquaresDigits(slow)
            fast = self.sumSquaresDigits(self.sumSquaresDigits(fast))
        return slow == fast == 1
