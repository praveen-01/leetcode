class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(arr,k):
            l=0
            r=len(arr)-1
            while l<=r:
                m=(l+r)//2
                if arr[m]==k:
                    return True
                elif arr[m]>k:
                    r=m-1
                else:
                    l=m+1
            return False
        for row in matrix:
            res=search(row,target)
            if res:
                return True
        return False
        