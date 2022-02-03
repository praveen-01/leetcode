class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i=0
        c=0
        j=k
        avg=sum(arr[i:j])/k
        if avg>=threshold:
            c+=1
           # print(arr[i:j])
        i+=1
        j+=1
        while j<=len(arr):
            avg+=arr[j-1]/k
            avg-=arr[i-1]/k
            if avg>=threshold:
                c+=1
                #print(arr[i:j])
            i+=1
            j+=1
        return c
        