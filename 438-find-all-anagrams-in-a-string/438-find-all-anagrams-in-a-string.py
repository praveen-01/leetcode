class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def equal(d1,d2):
            for i in d2:
                if i not in d1 or d1[i]!=d2[i]:
                    return False
            for i in d1:
                if d1[i]!=0:
                    if i not in d2 or d2[i]!=d1[i]:
                        return False
            return True
        d1={}
        c=[]
        a=0
        j=len(p)
        k=s[a:j]
        d={}
        for i in p:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        
        for i in k:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if equal(d,d1):
            c.append(a)
        j+=1
        a+=1
        while j<=len(s):
            ne=s[j-1]
            if ne not in d:
                d[ne]=1
            else:
                d[ne]+=1
            ol=s[a-1]
            d[ol]-=1
            if equal(d,d1):
                c.append(a)
            j+=1
            a+=1
        return c
                
                    