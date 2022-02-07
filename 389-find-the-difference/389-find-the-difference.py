class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        ls=len(s)
        ts=len(t)
        i=0
        s="".join(sorted(s))
        t="".join(sorted(t))
        while i<ls:
            if s[i]!=t[i]:
                return t[i]
            i+=1
        return t[-1]
        