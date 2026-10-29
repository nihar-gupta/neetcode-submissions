# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        mini = self.kSmallest(root, k)
        #total_count = self.getNodesCount(root)
        #maxi = self.kSmallest(root, total_count-k+1)
        return mini

    
    # def kLargest(self, root, k):
    #     if root == None: return None 

    #     count = self.getNodesCount(root.left, k)
    def kSmallest(self, root, k):
        if root == None: return None

        count = self.getNodesCount(root.left)
        if count+1 == k: return root.val
        if count >= k: return self.kSmallest(root.left, k)
        return self.kSmallest(root.right, k-count-1)

    
    def getNodesCount(self, root):
        if root==None: return 0

        k1 = self.getNodesCount(root.left)
        k2 = self.getNodesCount(root.right)
        return 1+k1+k2
        