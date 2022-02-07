# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        st=[]
        st.append(root)
        res=[]
        flag=0
        while st:
            r=[]
            for _ in range(len(st)):
                root=st.pop(0)
                if root:
                    r.append(root.val)
                if root.left:
                    st.append(root.left)
                if root.right:
                    st.append(root.right)
            if flag == 0:
                flag = 1
            else:
                r = r[::-1]
                flag = 0
            res.append(r)
                    
        return res
                
                
        