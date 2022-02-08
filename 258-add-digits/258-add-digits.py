class Solution:
    def addDigits(self, num: int) -> int:
        def recur(num):
            s=0
            while num>0:
                re=num%10
                s=s+re
                num=num//10
            return s
        if num<10:
            return num
        while num>=10:
            num=recur(num)
        return num