# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root, mini):
            nonlocal c
            if root is None: return

            if root.val >= mini: 
                c+=1
                mini = root.val
            solve(root.left, mini)
            solve(root.right, mini)


        c = 0
        solve(root, float('-inf'))
        return c

