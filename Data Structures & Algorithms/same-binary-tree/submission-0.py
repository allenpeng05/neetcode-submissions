# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check for base cases of p = None and/or q = None
        if not p and not q:
            return True
        if not p or not q:
            return False
        # if both p and q have valid values, compare them
        if p.val != q.val:
            return False
        # recursively call on left and right subtree
        # AND all checks to ensure everything returns True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        