# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            nonlocal ans
            if root == None: return 0

            p1 = max(solve(root.left), 0)
            p2 = max(solve(root.right), 0)
            
            ans = max(ans, p1+p2+root.val)

            return max(p1,p2) + root.val 

        ans = float('-inf')
        solve(root)
        return ans
        