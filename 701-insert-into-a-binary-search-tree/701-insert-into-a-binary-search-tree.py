# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root,key):
            if not root:
                return TreeNode(key)
            else:
                if root.val>key:
                    root.left=insert(root.left,key)
                else:
                    root.right=insert(root.right,key)
            return root
        return insert(root,val)
        