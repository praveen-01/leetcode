class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi=0
        i=0
        while i<len(nums):
            maxi+=min(nums[i],nums[i+1])
            i=i+2
        return maxi
        
        