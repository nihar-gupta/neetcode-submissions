# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        stack = []
        stack.append(root)
        while len(stack) > 0:
            curr = stack.pop()
            if curr.val == subRoot.val:
                check = self.isSameTree(curr, subRoot)
                if check: return True 
            
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
        return False


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True 
        if p is None or q is None: return False

        if p.val != q.val: return False 

        r1 = self.isSameTree(p.left, q.left)
        if not r1: return False

        r2 = self.isSameTree(p.right, q.right)
        if not r2: return False

        return True
            
        