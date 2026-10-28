# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def solve(root, level):
            nonlocal d
            if root is None: return 

            
            d[level]= root.val

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
        