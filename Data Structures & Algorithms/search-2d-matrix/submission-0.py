class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top, bottom = 0, len(matrix) - 1
        cols = len(matrix[0]) - 1

        target_row = -1

        # find row
        while top <= bottom:
            mid_row = (top + bottom) // 2

            # at the right row
            if matrix[mid_row][0] <= target <= matrix[mid_row][cols]:
                target_row = mid_row
                break

            if matrix[mid_row][cols] > target:
                bottom = mid_row - 1
            else:
                top = mid_row + 1

        if target_row == -1:
            return False

        left, right = 0, cols    
        while left <= right:
            mid_col = (left + right) // 2

            val = matrix[target_row][mid_col]

            if val == target:
                return True
            elif val > target:
                right = mid_col - 1
            else:
                left = mid_col + 1
        
        return False
            
