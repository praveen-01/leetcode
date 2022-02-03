class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d={}
        for i in nums1:
            for j in nums2:
                p=-(i+j)
                if p in d:
                    d[p]+=1
                else:
                    d[p]=1
        c=0
        for i in nums3:
            for j in nums4:
                l=i+j
                if l in d:
                    c+=d[l]
        return c