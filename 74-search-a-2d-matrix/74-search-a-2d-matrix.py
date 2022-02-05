class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h=len(matrix)
        w=len(matrix[0])
        y=h-1
        x=0
        while True:
            if y<0 or x>=w:
                break
            if target<matrix[y][x]:
                y-=1
            elif target>matrix[y][x]:
                x+=1
            else:
                return True
        return False
        