class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        k=s.split()
        d={}
        if len(k)!=len(pattern):
            return False
        for i in range(0,len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]]!=k[i]:
                    return False
            else:
                d[pattern[i]]=k[i]
        d1={}
        for i in range(0,len(k)):
            if k[i] in d1:
                if d1[k[i]]!=pattern[i]:
                    return False
            else:
                d1[k[i]]=pattern[i]
                
        return True
        