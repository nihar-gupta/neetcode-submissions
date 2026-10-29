# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        #your code goes here
        if len(inorder) == 0: return None 

        def construct(
                        preorder, prestart, preend, 
                        inorder, instart, inend,
                        inorder_dict
                    ):

            # no elements left - so return None        
            if prestart > preend or instart > inend: return None 

            # Inorder: LDR 
            # Preorder: DLR 

            # Preorder's first element is root 

            root = TreeNode(preorder[prestart])
            inorder_idx = inorder_dict[preorder[prestart]]

            # all the elements left in inorder are towards left side of the root 
            # all the elements right in inorder are towards right side of the root 

            no_of_left_nodes = inorder_idx - instart

            root.left = construct(
                                    preorder, prestart+1, prestart+no_of_left_nodes,
                                    inorder,  instart, inorder_idx - 1,
                                    inorder_dict,
                                )

            root.right = construct(
                                    preorder,  prestart+no_of_left_nodes+1, preend, 
                                    inorder,   inorder_idx +1, inend,
                                    inorder_dict
                                )

            return root 


        inorder_dict = dict()
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i
        
        return construct(
                            preorder, 0, len(preorder)-1,
                            inorder,  0, len(inorder)-1,
                            inorder_dict, 
                        )
        