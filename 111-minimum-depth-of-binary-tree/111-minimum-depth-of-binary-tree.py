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
        r=1
        st=[]
        st.append(root)
        lev=[]
        while st:
            for k in st:
                if k.left==None and k.right==None:
                    return r
                if k.left:
                    lev.append(k.left)
                if k.right:
                    lev.append(k.right)
            r+=1
            st=lev
            lev=[]
            
        
                    
            
        