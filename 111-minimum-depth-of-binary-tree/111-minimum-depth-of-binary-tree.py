# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st=[]
        le=[]
        st.append(root)
        r=1
        while st:
            for root in st:
                if root.left==None and root.right==None:
                    return r
                if root.left:
                    le.append(root.left)
                if root.right:
                    le.append(root.right)
            r+=1
            st=le
            le=[]
            
        