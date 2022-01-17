class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st={}
        ts={}
        for c1,c2 in zip(s,t):
            if c1 not in st and c2 not in ts:
                st[c1]=c2
                ts[c2]=c1
            elif st.get(c1)!=c2 or ts.get(c2)!=c1:
                return False
        return True
        