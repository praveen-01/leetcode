# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        s=[]
        s.append(cloned)
        while s:
            k=s.pop()
            if k:
                if k.val==target.val:
                    return k
                s.append(k.left)
                s.append(k.right)
        
        