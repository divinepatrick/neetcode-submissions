# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getHeight(root)
        return self.diameter

    def getHeight(self, root):
        if not root:
            return 0
        L = self.getHeight(root.left)
        R = self.getHeight(root.right)

        self.diameter = max(self.diameter, L + R)
        return max(L, R) + 1