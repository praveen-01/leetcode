class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=[]
        for i in nums:
            if d[i]==1 and i+1 not in d and i-1 not in d:
                ans.append(i)
        return ans
        