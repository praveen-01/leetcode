class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[0]*n
        lis[0]=1
        if n==1:
            return 1
        for i in range(1,n):
            lis[i]=1
            for j in range(0,i):
                if nums[i]>nums[j] and lis[i]<lis[j]+1:
                    lis[i]=lis[j]+1
        return max(lis)
        
        