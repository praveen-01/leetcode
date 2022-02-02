class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l=0
        h=len(nums)-1
        if nums[0]<nums[h]:
            return nums[0]
        while l<=h:
            m=(l+h)//2
            if nums[m]<nums[m-1]:
                return nums[m]
            if nums[m+1]<nums[m]:
                return nums[m+1]
            if nums[m]>nums[0]:
                l=m+1
            else:
                h=m-1
        
            