# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # T: O(N) | S: O(Leaves)
        # Leaves = N
        if not root:
            return None
        stack = [root]
        while stack:
            next_stack = []
            for _ in range(len(stack)):
                node = stack.pop()
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
                if node.left or node.right:
                    node.left, node.right = node.right, node.left
            while next_stack:
                stack.append(next_stack.pop())
        return root

    # Recursive
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     # T: O(N) | S: O(Height)
    #     # Height = O(LOG N) / O(N)
    #     if not root:
    #         return None
    #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root
