# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def level(root):
            d={}
            s=[]
            s.append([root,0])
            ans=[]
            while s:
                l,k=s.pop()
                if l:
                    if len(ans)==k:
                        ans.append([l.val])
                    else:
                        ans[k].append(l.val)
                    s.append([l.left,k+1])
                    s.append([l.right,k+1])
            return ans
        return sum(level(root)[-1])
        