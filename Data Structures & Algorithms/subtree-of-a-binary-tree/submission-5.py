# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # T: O(M) | S: O(H)
        # H = Height of the subroot = O(LOG M) / O(M)
        if not(p or q):
            return True
        if not(p and q) or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # T: O(N) | S: O(H)
        # H = Height of the root = O(LOG N) / O(N)
        if not root:
            return False
        is_left_subtree = self.isSubtree(root.left, subRoot)
        is_right_subtree = self.isSubtree(root.right, subRoot)
        if not(is_left_subtree or is_right_subtree):
            return self.isSameTree(root, subRoot)
        return True
