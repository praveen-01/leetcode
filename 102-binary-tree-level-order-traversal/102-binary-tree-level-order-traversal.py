# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        q.append([root,0])
        ans=[]
        while q:
            l,k=q.pop(0)
            if l:
                if len(ans)==k:
                    ans.append([l.val])
                else:
                    ans[k].append(l.val)
                q.append([l.left,k+1])
                q.append([l.right,k+1])
        return ans