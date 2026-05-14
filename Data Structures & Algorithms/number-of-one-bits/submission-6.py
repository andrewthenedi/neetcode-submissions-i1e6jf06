class Solution:
    def hammingWeight(self, n: int) -> int:
        # T: O(N) | S: O(1)
        solution = 0
        while n:
            solution += 1
            n &= (n - 1)
        return solution

        # # T: O(N) | S: O(1)
        # solution = 0
        # while n:
        #     solution += n & 1
        #     n >>= 1
        # return solution
