# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS helper tracks height and diameter
# 1) height: longest downward path from this node
# need height bc the diameter through a node depends on the heights of its left and right subtrees

# 2) diameter: longest path found anywhere in this subtree
# biggest diameter may or may not pass through current node(current diameter)
# best_d = max of curr_d, left_d, right_d
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            left_h, left_d = dfs(root.left)
            right_h, right_d = dfs(root.right)
            h = 1 + max(left_h, right_h)

            curr_d = left_h + right_h
            best_d = max(curr_d , left_d, right_d)

            return h, best_d
        return dfs(root)[1]


        

        