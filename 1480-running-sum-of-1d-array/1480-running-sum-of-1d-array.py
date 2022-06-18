class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        su=[]
        su.append(nums[0])
        for i in range(1,len(nums)):
            su.append(su[i-1]+nums[i])
        return su