class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        od=0
        nu=0
        if len(d)==1:
            return len(s)
        for i in d:
            if d[i]%2==0:
                c+=d[i]
            else:
                if nu==0:
                    c+=d[i]
                    nu=1
                else:
                    c+=d[i]-1
        return c
        