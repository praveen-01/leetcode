# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        s=[]
        ans=[]
        s.append([root,0])
        while s:
            root,l=s.pop(0)
            if root:
                if len(ans)==l:
                    ans.append([root.val])
                else:
                    ans[l].append(root.val)
                s.append([root.left,l+1])
                s.append([root.right,l+1])
        return ans
        