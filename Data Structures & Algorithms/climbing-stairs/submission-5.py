class Solution:
    def climbStairs(self, n: int) -> int:
        # T: O(N) | S: O(1)
        first, second = 1, 2
        if n < 3:
            return second if n == second else first
        for _ in range(n - 2):
            first, second = second, first + second
        return second
