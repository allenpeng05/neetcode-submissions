# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # helper function to determine if two trees are the same
        def sameTree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        # base case: empty tree can not have subtree
        # if we recurse all the way down a path of root and still don't have a match, return False
        if not root:
            return False

        # if the two trees are the same, return True
        if sameTree(root, subRoot):
            return True
        # use DFA to check equality of every subtree of root against subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        