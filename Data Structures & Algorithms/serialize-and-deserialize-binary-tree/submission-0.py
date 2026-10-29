# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:



        """
        :type root: TreeNode
        :rtype: string
        """
        rt = []
        stack = []
        stack.append(root)
        if root:
            rt.append(root.val)
        else:
            rt.append(None)

        i=0
        while i<len(stack):
            if stack[i]:
                
                if stack[i].left:
                    rt.append(stack[i].left.val)
                    stack.append(stack[i].left)
                else:
                    rt.append(None)
                    stack.append(None)

                if stack[i].right:
                    rt.append(stack[i].right.val)
                    stack.append(stack[i].right)
                else:
                    rt.append(None)
                    stack.append(None)
            
            i+=1
        rtt = ""
        for i in rt:
            if i is None:
                rtt += "N,"
            else:
                rtt = rtt + str(i) + ","
        return rtt


        
    # Decodes your encoded val to tree.
    def deserialize(self, val: str) -> Optional[TreeNode]:

        """
        :type root: string
        :rtype: TreeNode
        """
        valll = val.split(",")
        #print(valll)
        val = []
        for i in range(len(valll)-1):
            if valll[i] == "N": 
                val.append(None)
            else:
                val.append(int(valll[i]))
            


        if val[0] == None: return None 

        root = TreeNode(val[0])
        curr = root 

        queue = []
        queue.append(root)
        j = 0

        i = 1
        while i<len(val)-1:
            if val[i]:
                left = TreeNode(val[i])
                queue[j].left = left 
                queue.append(left)
            
            if val[i+1]:
                right = TreeNode(val[i+1])
                queue[j].right = right
                queue.append(right)
            
            j+=1
            i+=2
        
        return root