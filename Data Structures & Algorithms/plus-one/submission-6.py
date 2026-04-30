class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # T: O(N) | S: O(N)
        result = []
        carry = 1
        for digit in reversed(digits):
            num = digit + carry
            carry = num // 10
            result.append(num % 10)
        if carry:
            result.append(carry)
        result.reverse()
        return result
