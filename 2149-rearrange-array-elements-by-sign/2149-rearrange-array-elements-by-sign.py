class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        i=0
        k=0
        ans=[]
        while k<len(pos):
            ans.append(pos[k])
            ans.append(neg[k])
            k+=1
        return ans
        