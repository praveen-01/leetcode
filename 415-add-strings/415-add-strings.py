class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        def num(st):
            i=0
            s=0
            while i<len(st):
                s=s*10+d[st[i]]
                i+=1
            return s
        res=num(num1)+num(num2)
        return str(res)