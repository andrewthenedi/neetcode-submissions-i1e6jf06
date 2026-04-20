# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursive(self, node: Optional[TreeNode]) -> tuple[int, int]:
        # T: O(N) | S: O(H)
        # O(H) = O(LOG N) / O(N)
        if not node:
            return -1, -1
        left_height, left_diameter = self.recursive(node.left)
        right_height, right_diameter = self.recursive(node.right)
        max_height = 1 + max(left_height, right_height)
        curr_diameter = 2 + left_height + right_height
        max_diameter = max(curr_diameter, left_diameter, right_diameter)
        return max_height, max_diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, max_diameter = self.recursive(root)
        return max_diameter
