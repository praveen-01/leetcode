class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=(len(arr)-k)%len(arr)
        l=arr[a:]+arr[:a]
        for i in range(0,len(arr)):
            arr[i]=l[i]
            
        