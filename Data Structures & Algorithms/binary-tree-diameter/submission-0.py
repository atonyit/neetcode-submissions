# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #returns height
        def dfs(node):
            if not node:
                return 0

            #gets heights of subtree
            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(self.res, left + right)

            #calculate height then add 1 for current one were at
            return max(left, right) + 1

        dfs(root)
        return self.res
