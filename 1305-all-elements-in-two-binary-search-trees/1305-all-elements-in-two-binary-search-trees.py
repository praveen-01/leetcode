# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root,arr):
            if root:
                inorder(root.left,arr)
                arr.append(root.val)
                inorder(root.right,arr)
        arr1=[]
        arr2=[]
        inorder(root1,arr1)
        inorder(root2,arr2)
        arr1.extend(arr2)
        arr1.sort()
        return arr1
            
        