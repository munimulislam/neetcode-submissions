class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        s = 0
        e = len(matrix) -1
        
        while s <= e:
            m = (s+e) // 2

            if target < matrix[m][0]:
                e = m - 1
            elif target > matrix[m][-1]:
                s = m + 1
            else:
                break
        
        s = 0
        e = len(matrix[m]) - 1

        while s <= e:
            row_m = (s+e) // 2
            if target < matrix[m][row_m]:
                e = row_m - 1
            elif target > matrix[m][row_m]:
                s = row_m + 1
            else:
                return True
        
        return False