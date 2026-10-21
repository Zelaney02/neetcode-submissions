class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        low = 0
        high = (col * row) - 1

        while low <= high:
            mid = (low + high) // 2

            r = mid // col # floor division accounts for starting at 0 index
            c = mid % col
            mid_value = matrix[r][c] # use imaginary 1d array, align and convert

            if mid_value == target:
                return True
            elif mid_value < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


        