class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        cur=intervals[0][1]
        i=1
        ans=0
        while i<len(intervals):
            if cur>intervals[i][0]:
                ans+=1
            else:
                cur=intervals[i][1]
            i+=1
        return ans