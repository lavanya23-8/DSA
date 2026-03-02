class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n-1

        while left <= right:
            mid = (left +right)//2

            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False                    