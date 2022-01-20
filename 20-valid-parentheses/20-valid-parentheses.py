class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i=="[" or i=="{" or i=="(":
                st.append(i)
            else:
                if len(st)==0:
                    return False
                if i==")":
                    if st[-1]!="(" or len(st)==0:
                        return False
                if i=="}":
                    if st[-1]!="{" or len(st)==0:
                        return False
                if i=="]":
                    if st[-1]!="[" or len(st)==0:
                        return False
                st.pop()
        if len(st)>0:
            return False
        return True
                    
        