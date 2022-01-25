# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(root,subsum):
            ans=0
            subsum=subsum-root.val
            if subsum==0 and root.left==None and root.right==None:
                return True
            if root.left:
                ans=ans or path(root.left,subsum)
            if root.right:
                ans=ans or path(root.right,subsum)
            return ans
        if not root:
            return False
        return path(root,targetSum)
            
        