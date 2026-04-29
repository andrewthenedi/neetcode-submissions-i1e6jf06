class Solution:
    def climbStairs(self, n: int) -> int:
        # T: O(N) | S: O(1)
        if n <= 2:
            return n
        first, second = 1, 2
        for _ in range(n - 2):
            first, second = second, first + second
        return second
