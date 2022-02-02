class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x==1:
            return 1
        l=1
        r=x
        while l<=r:
            m=(l+r)//2
            if m*m==x:
                return m
            if m*m<x and (m+1)*(m+1)>x:
                return m
            if m*m>x:
                r=m-1
            else:
                l=m+1
        