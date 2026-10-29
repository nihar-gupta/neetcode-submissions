# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root, mini, maxi):
            if root is None: return True

            if mini >= root.val or root.val >= maxi:
                return False
            
            return (
                        solve(root.left, mini, root.val) and
                        solve(root.right, root.val, maxi)
                    )
        return solve(root, float('-inf'), float('inf'))

