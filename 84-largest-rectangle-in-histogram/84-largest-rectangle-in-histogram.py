class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair (index, h)
        
        # calculate the part have increasing high in the histogram
        for i, h in enumerate(heights):
            start = i
            
            # find the smallest index the heights[i] could extent to.
            while stack and stack[-1][1] > h:
                index, high = stack.pop()
                # calculate the area of increasing part before i
                maxArea = max(maxArea, high * (i - index))
                start = index
            
            stack.append((start, h))
        
        # the remain part in the stack will also be increasing high
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea
        