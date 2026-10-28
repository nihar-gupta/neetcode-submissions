# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            nonlocal ans
            if root is None: return 0
            #if root.left is None and root.right is None: return 0

            k = solve(root.left)
            p = solve(root.right)
            ans = max(ans, k+p+1)
            return max(k,p)+1
        
        ans = 0
        solve(root)
        return ans-1