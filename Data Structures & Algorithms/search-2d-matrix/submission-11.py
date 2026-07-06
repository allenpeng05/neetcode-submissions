class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            midpoint = l + (r - l) // 2
            row = midpoint // cols
            col = midpoint % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = midpoint - 1
            else:
                l = midpoint + 1
        
        return False
        


        