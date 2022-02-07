class Solution:
    def findMin(self, nums: List[int]) -> int:
        size=len(nums)
        if size==1:
            return nums[0]
        l=0
        h=size-1
        if nums[l]<nums[h]:
            return nums[l]
        while l<=h:
            m=(l+h)//2
            if nums[m]>nums[m+1]:
                return nums[m+1]
            if nums[m]<nums[m-1]:
                return nums[m]
            if nums[m]>nums[0]:
                l=m+1
            else:
                h=m-1
                
        
            