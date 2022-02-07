# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        st=[]
        res=[]
        st.append([root,0])
        while st:
            root,le=st.pop(0)
            if root:
                if le==len(res):
                    res.append([root.val])
                else:
                    res[le].append(root.val)
                st.append([root.left,le+1])
                st.append([root.right,le+1])
        return res[::-1]