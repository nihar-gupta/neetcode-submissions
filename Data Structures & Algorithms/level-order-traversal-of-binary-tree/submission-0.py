# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solve(root, level):
            nonlocal d
            if root is None: return 

            if level not in d: d[level] = []
            d[level].append(root.val)

            solve(root.left, level+1)
            solve(root.right, level+1)
            

        d = dict()
        solve(root, 0)
        rt = []
        i=0
        while i in d:
            rt.append(d[i])
            i+=1
        return rt

        