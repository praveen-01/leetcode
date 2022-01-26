# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low_thres, high_thres):
            if node == None:
                return True
            return low_thres < node.val < high_thres and validate(node.left, low_thres, node.val) and validate(node.right, node.val, high_thres)
        
        return validate(root.left, float('-inf'), root.val) and validate(root.right, root.val, float('inf'))
        