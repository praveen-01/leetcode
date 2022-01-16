class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x :x[0])
        ans=[]
        ans.append(intervals[0])
        for inter in intervals:
            if inter[0]<=ans[-1][1]:
                ans[-1][1]=max(ans[-1][1],inter[1])
            else:
                ans.append(inter)
        return ans
        