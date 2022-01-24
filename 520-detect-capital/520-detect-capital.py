class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c=0
        for i in word:
            if i.isupper():
                c+=1
        if c==len(word):
            return True
        if c==0:
            return True
        if c==1 and word[0].isupper():
            return True
        return False
        