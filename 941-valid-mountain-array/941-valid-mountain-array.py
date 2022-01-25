class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        res=-1
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                res=i
                break
        if res==-1:
            return False
        k=0
        while k<res:
            if arr[k+1]<=arr[k]:
                return False
            k=k+1
        k=res+1
        while k<len(arr):
            if arr[k-1]<=arr[k]:
                return False
            k=k+1
        return True
        
        
            
        