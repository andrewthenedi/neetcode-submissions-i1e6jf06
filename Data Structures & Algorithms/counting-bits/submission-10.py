class Solution:
    def getCountOnes(self, n: int) -> int:
        # T: O(number of 1 bits in n) | S: O(1)
        count_ones = 0
        while n:
            count_ones += 1
            n &= (n - 1)
        return count_ones

    def countBits(self, n: int) -> List[int]:
        # T: O(N LOG N) | S: O(N)
        output = []
        for i in range(n + 1):
            output.append(self.getCountOnes(i))
        return output
