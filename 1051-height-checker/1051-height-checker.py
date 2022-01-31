class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex=[i for i in heights]
        ex.sort()
        c=0
        for i in range(0,len(heights)):
            if heights[i]!=ex[i]:
                c+=1
        return c
        