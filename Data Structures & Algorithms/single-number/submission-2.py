class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # T: O(N) | S: O(1)
        unique = 0
        for num in nums:
            unique ^= num
        return unique
