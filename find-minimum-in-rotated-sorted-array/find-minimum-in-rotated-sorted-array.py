class Solution:
    def findMin(self, nums: List[int]) -> int:
        size=len(nums)
        if size==1:
            return nums[0]
        l=0
        r=size-1
        if nums[l]<nums[r]:
            return nums[l]
        while l<=r:
            m=l+(r-l)//2
            if nums[m]>nums[m+1]:
                return nums[m+1]
            if nums[m]<nums[m-1]:
                return nums[m]
            if nums[m]>nums[l]:
                l=m+1
            else:
                r=m-1
                
        
            