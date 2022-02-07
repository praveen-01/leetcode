class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def sear(arr,l,h,key):
            if l>h:
                return -1
            m=(l+h)//2
            if arr[m]==key:
                return m
            if arr[l]<=arr[m]:
                if key>=arr[l] and key<=arr[m]:
                    return sear(arr,l,m-1,key)
                return sear(arr,m+1,h,key)
            else:
                if key>=arr[m] and key<=arr[h]:
                    return sear(arr,m+1,h,key)
                return sear(arr,l,m-1,key)
            
        return sear(nums,0,len(nums)-1,target)
                    
            