class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c=0
        d={0:-1}
        maxi=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                c-=1
            if nums[i]==1:
                c+=1
            if c not in d:
                d[c]=i
            else:
                maxi=max(maxi,i-d[c])
        return maxi
            
        