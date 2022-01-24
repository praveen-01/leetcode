class Solution:
    def isPalindrome(self, x: int) -> bool:
        k=0
        s=0
        l=x
        while l>0:
            re=l%10
            s=s*10+re
            l=l//10
        return s==x
        