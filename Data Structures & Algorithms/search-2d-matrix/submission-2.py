class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            start = 0
            end = len(matrix[i])-1
            if matrix[i][end] < target:
                continue
            mid = (start + end) // 2
            while (start <= end):
                if target > matrix[i][mid]:
                    start = mid + 1
                elif target < matrix[i][mid]:
                    end = mid - 1
                else:
                    return True
                mid = (start + end) // 2
        return False