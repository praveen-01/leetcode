class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(nums)
        if k<3:
            return k
        c=1
        cur=nums[0]
        i=1
        while i<len(nums):
            if nums[i]==cur and c<2:
                c+=1
                i+=1
            elif nums[i]!=cur:
                cur=nums[i]
                c=1
                i+=1
            elif c>=2:
                del nums[i]
        return len(nums)
                
            