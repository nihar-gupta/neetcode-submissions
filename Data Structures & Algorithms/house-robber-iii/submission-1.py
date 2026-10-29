# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(root, prev):
            nonlocal d
            if root is None: return 0

            if root in d: 
                if prev:
                    if d[root][0] is not False:
                        return d[root][0]
                else:
                    if d[root][1] is not False:
                        return d[root][1]
            d[root] = [False, False]

            if prev:
                p1 = solve(root.left, False)
                p2 = solve(root.right, False)
                rt = p1+p2
                d[root][0] = rt
            
            else:
                k1 = solve(root.left, False)
                k2 = solve(root.right, False)

                p1 = solve(root.left, True)
                p2 = solve(root.right, True)

                d[root][0] = k1+k2
                d[root][1] = max(k1+k2, p1+p2+root.val)
                return max(k1+k2, p1+p2+root.val)
        d = dict()
        return solve(root, False)

        