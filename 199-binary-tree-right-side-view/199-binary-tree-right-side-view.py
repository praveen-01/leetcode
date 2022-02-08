# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        st=[]
        res=[]
        st.append([root,0])
        while st:
            root,le=st.pop(0)
            if root:
                if len(res)==le:
                    res.append([root.val])
                else:
                    res[le].append(root.val)
                st.append([root.left,le+1])
                st.append([root.right,le+1])
        ans=[]
        for level in res:
            ans.append(level[-1])
        return ans
        