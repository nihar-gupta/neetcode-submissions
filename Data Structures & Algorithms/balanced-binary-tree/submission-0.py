# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(root):
            if root is None: return True, 0

            k1, k2 = solve(root.left)
            p1, p2 = solve(root.right)

            if k1 and p1:
                if abs(k2-p2) <= 1:
                    # valid 
                    return True, max(k2,p2) +1
                else:
                    return False, float('inf')
            else:
                return False, float('inf')
        return solve(root)[0]


        